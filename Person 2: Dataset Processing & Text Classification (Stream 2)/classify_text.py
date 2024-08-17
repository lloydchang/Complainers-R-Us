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

def split_text(text, max_length=512):
    """Split text into chunks of a specified maximum length."""
    tokenizer = classifier.tokenizer
    tokens = tokenizer.encode(text, truncation=False)
    for i in range(0, len(tokens), max_length):
        yield tokenizer.decode(tokens[i:i + max_length], skip_special_tokens=True)

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

    # Split and classify the text in chunks
    for chunk in split_text(transcribed_text):
        classify_text(chunk)

except FileNotFoundError:
    print(f"The file '{transcribed_text_file}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
