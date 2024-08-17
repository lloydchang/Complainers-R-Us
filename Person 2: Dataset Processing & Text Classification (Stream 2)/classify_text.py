from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer
import torch
print(torch.cuda.is_available())
from concurrent.futures import ThreadPoolExecutor, as_completed

# Check CUDA availability
if not torch.cuda.is_available():
    raise RuntimeError("CUDA is not available. Ensure PyTorch is installed with CUDA support.")

# Load model and tokenizer
model_name = 'distilbert-base-uncased-finetuned-sst-2-english'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Set up model for multi-GPU
if torch.cuda.device_count() > 1:
    model = torch.nn.DataParallel(model)

model.to('cuda')  # Move model to GPU

def classify_text(text):
    """Classify the given text and return results."""
    inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to('cuda')
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    predicted_class = torch.argmax(probabilities, dim=-1).item()
    return {
        'label': 'POSITIVE' if predicted_class == 1 else 'NEGATIVE',
        'score': probabilities[0][predicted_class].item()
    }

def split_text_into_chunks(text, max_length=512):
    """Split text into chunks of a specified maximum length."""
    tokens = tokenizer.encode(text, truncation=False)
    chunks = [tokenizer.decode(tokens[i:i + max_length], skip_special_tokens=True) 
              for i in range(0, len(tokens), max_length)]
    return chunks

def process_chunks_in_parallel(chunks):
    """Process text chunks in parallel using multiple GPUs."""
    results = []
    with ThreadPoolExecutor() as executor:
        future_to_chunk = {executor.submit(classify_text, chunk): chunk for chunk in chunks}
        for future in as_completed(future_to_chunk):
            chunk = future_to_chunk[future]
            try:
                result = future.result()
                results.append((chunk, result))
            except Exception as exc:
                print(f'Chunk processing generated an exception: {exc}')
    return results

# Test classification with simple text
test_texts = [
    "I love using GPUs for deep learning!",
    "I love using Hugging Face models!"
]

for text in test_texts:
    result = classify_text(text)
    print("\n")
    print(text)
    print(result)
    print("\n")

# Process text from file
transcribed_text_file = "cleaned_text.txt"

try:
    # Load transcribed text
    with open(transcribed_text_file, 'r') as file:
        transcribed_text = file.read()

    # Split text into chunks
    chunks = split_text_into_chunks(transcribed_text)

    # Process chunks in parallel
    results = process_chunks_in_parallel(chunks)

    # Print results
    for chunk, result in results:
        print("\n")
        print(chunk)
        print(result)
        print("\n")

except FileNotFoundError:
    print(f"The file '{transcribed_text_file}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
