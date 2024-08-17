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

# ❯ python classify_text.py
# /Users/lloyd/.pyenv/versions/3.12.4/lib/python3.12/site-packages/transformers/tokenization_utils_base.py:1601: FutureWarning: `clean_up_tokenization_spaces` was not set. It will be set to `True` by default. This behavior will be depracted in transformers v4.45, and will be then set to `False` by default. For more details check this issue: https://github.com/huggingface/transformers/issues/31884
#   warnings.warn(


# I love using GPUs for deep learning!
# [{'label': 'POSITIVE', 'score': 0.9990824460983276}]




# I love using Hugging Face models!
# [{'label': 'POSITIVE', 'score': 0.9992625117301941}]


# [{'label': 'NEGATIVE', 'score': 0.9947984218597412}]