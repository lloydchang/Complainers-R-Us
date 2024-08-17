from transformers import pipeline

# Initialize the classifier
classifier = pipeline('text-classification', model='distilbert-base-uncased-finetuned-sst-2-english', device=0)

def classify_text(text):
    """Classify the given text and print results."""
    result = classifier(text)
    print("\n")
    print(text)
    print(result)
    print("\n")

# Test classification with simple text
test_texts = [
    "I love using GPUs for deep learning!",
    "I love using Hugging Face models!"
]

for text in test_texts:
    classify_text(text)

# Process text from file
transcribed_text_file = "cleaned_text.txt"

try:
    # Load transcribed text
    with open(transcribed_text_file, 'r') as file:
        transcribed_text = file.read()

    # Tokenizer for handling long texts
    tokenizer = classifier.tokenizer
    inputs = tokenizer(transcribed_text, return_tensors='pt', truncation=True, padding=False, max_length=512)
    truncated_text = tokenizer.decode(inputs['input_ids'][0], skip_special_tokens=True)

    # Classify the truncated text
    results = classifier(truncated_text)

    # Print results
    print(results)

except FileNotFoundError:
    print(f"The file '{transcribed_text_file}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
