# classify_text.py

import torch
import time
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
import multiprocessing
import warnings
from transformers.utils import logging

# Suppress FutureWarning and other warnings
logging.set_verbosity_warning()
warnings.filterwarnings("ignore", category=UserWarning, module='transformers')

def get_mps_device_count():
    """Return the number of MPS devices."""
    return 1

# Check for MPS, then CUDA, then fallback to CPU
if torch.backends.mps.is_available():
    device = torch.device("mps")
    mps_device_count = get_mps_device_count()
    print(f"Using MPS. Number of MPS devices: {mps_device_count}.")
elif torch.cuda.is_available():
    device = torch.device("cuda")
    gpu_device_count = torch.cuda.device_count()
    print(f"Using CUDA. Number of GPUs: {gpu_device_count}.")
else:
    device = torch.device("cpu")
    cpu_device_count = os.cpu_count()
    print(f"Neither MPS nor CUDA is available. Falling back to CPU. Number of CPUs: {cpu_device_count}.")

# Test device timing
start_time = time.time()

if device.type == "cpu":
    print("Running on CPU.")
    # Run CPU benchmark
    a = torch.ones(4000, 4000, device=device)
    for _ in range(200):
        a += a
else:
    if device.type == "cuda":
        torch.cuda.synchronize()
    elif device.type == "mps":
        torch.mps.synchronize()

    # Run GPU benchmark
    a = torch.ones(4000, 4000, device=device)
    for _ in range(200):
        a += a

elapsed_time = time.time() - start_time
print(f"{device.type.upper()} Time: {elapsed_time}")

print(f"CUDA Available: {torch.cuda.is_available()}")
print(f"CUDA Version: {torch.version.cuda if torch.cuda.is_available() else 'N/A'}")
print(f"Number of GPUs: {torch.cuda.device_count() if torch.cuda.is_available() else 0}")

# Load model and tokenizer
model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Set up model for multi-GPU if CUDA is available
if torch.cuda.device_count() > 1 and device.type == "cuda":
    model = torch.nn.DataParallel(model)

model.to(device)  # Move model to selected device

def classify_text(text, device):
    """Classify the given text and return results."""
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(device)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    return {
        'label': 'POSITIVE' if predicted_class == 1 else 'NEGATIVE',
        'score': probabilities[0][predicted_class].item()
    }

def split_text_into_chunks(data, max_length=512):
    """Split text into chunks of a specified maximum length, including IDs."""
    chunks = []
    for item in data:
        text = item['text']
        tokens = tokenizer.encode(text, truncation=False)
        # Ensure that tokens are truncated to fit the model's max length
        text_chunks = [tokenizer.decode(tokens[i:i + max_length], skip_special_tokens=True) 
                      for i in range(0, len(tokens), max_length)]
        for chunk in text_chunks:
            chunks.append({
                'chunk': chunk,
                'original_data': item
            })
    return chunks

def save_results_to_files(results):
    """Save classification results to files named by _id and complaint_id."""
    os.makedirs('results', exist_ok=True)
    for result in results:
        chunk = result['chunk']
        classification = result['classification']
        original_data = result['original_data']
        _id = original_data['_id']
        complaint_id = original_data['complaint_id']
        filename = f"results/_id-{_id}-complaint_id-{complaint_id}.txt"
        with open(filename, 'w') as file:
            file.write(f"Original Data:\n{json.dumps(original_data, indent=2)}\n\n")
            file.write(f"Chunk:\n{chunk}\n\n")
            file.write(f"Result:\n{json.dumps(classification, indent=2)}\n")

def worker(chunk, model, tokenizer, device):
    """Worker function for multiprocessing."""
    return {
        'chunk': chunk['chunk'],
        'classification': classify_text(chunk['chunk'], device),
        'original_data': chunk['original_data']
    }

def classify_chunks(chunks, device_type, device_ids):
    """Classify text chunks using multiprocessing and streams for GPU or MPS."""
    num_workers = os.cpu_count()
    results = []

    if device_type == 'cpu':
        with multiprocessing.Pool(processes=num_workers) as pool:
            results = [pool.apply_async(worker, (chunk, model, tokenizer, device)) 
                       for chunk in chunks]
            results = [result.get() for result in results]
    else:
        # For CUDA and MPS, process chunks using ThreadPoolExecutor for simplicity
        with ThreadPoolExecutor() as executor:
            future_to_chunk = {executor.submit(worker, chunk, model, tokenizer, torch.device(f"{device_type}:{device_id % len(device_ids)}")): chunk for chunk, device_id in zip(chunks, range(len(chunks)))}
            results = [future.result() for future in as_completed(future_to_chunk)]

    return results

# Process text from file
transcribed_text_file = "cleaned_text.jsonl"

try:
    # Load transcribed text
    with open(transcribed_text_file, 'r') as file:
        text_data = [json.loads(line) for line in file]

    # Split text into chunks with IDs
    chunks = split_text_into_chunks(text_data)

    # Determine device type and IDs
    device_type = device.type
    device_ids = list(range(torch.cuda.device_count())) if device_type == 'cuda' else list(range(get_mps_device_count()))

    # Process chunks using parallelism
    results = classify_chunks(chunks, device_type, device_ids)

    # Save results to files
    save_results_to_files(results)

except FileNotFoundError:
    print(f"The file '{transcribed_text_file}' was not found.")
except json.JSONDecodeError:
    print("Error decoding JSON from the file.")
except Exception as e:
    print(f"An error occurred: {e}")
