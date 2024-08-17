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

    # Tokenize and check if the text is too long for the model
    tokenizer = classifier.tokenizer
    inputs = tokenizer(transcribed_text, return_tensors='pt', truncation=False, padding=False)
    if len(inputs['input_ids'][0]) > 512:
        print("The text is too long and will be truncated.")
        # Truncate the text to the first 512 tokens
        transcribed_text = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs['input_ids'][0][:512]))

    # Classify the text
    results = classifier(transcribed_text)

    # Print results
    print(results)

except FileNotFoundError:
    print(f"The file '{transcribed_text_file}' was not found.")

except Exception as e:
    print(f"An error occurred: {e}")
