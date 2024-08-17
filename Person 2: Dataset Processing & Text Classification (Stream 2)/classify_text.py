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

    print("\n")
    print(truncated_text)
    # Print results
    print(results)
    print("\n")

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




# " xxxx xxxx xxxx xxxx xxxx xxxx xxxx ny xxxx xxxx xxxx date to macys xxxx inc xxxx xxxx xxxx xxxxxxxx xxxx xxxx ny xxxx attn xxxx xxxx executive office dear xxxx xxxx my name is xxxx xxxx and i am writing to address the ongoing issues with my macys credit account account number xxxx despite multiple attempts to resolve these matters over the phone i have not received the necessary assistance to correct the inaccuracies on my account xxxx disputed charge and lack of support i have called macys customer service many times to dispute a charge of 3100 and address other concerns each time the representatives were either unwilling or unable to assist me effectively macys should have records of these calls to verify my repeated efforts xxxx late fee i acknowledge the late fee of 3100 charged on xxxxyear and its subsequent credit on xxxxyear however this does not resolve the main issue of incorrect reporting xxxx credit reporting inaccuracy my account was reported as 30 days delinquent in xxxxyear i have consistently disputed this information stating that payments for xxxx and xxxxyear were made but not properly applied to my account additional impact due to this delinquency on my credit report my auto insurance increased to 33000 per month this has been a significant financial burden i request that macys conduct a comprehensive review including the phone call records and correct the inaccuracies on my account additionally i request the removal of the disputed by consumer note from my credit report once the issue is resolved additionally i do not want any macys advertisements sent to my apartment i hope to resolve this matter amicably and promptly thank you for your attention to this important issue sincerely xxxx xxxx " timely payments are always a priority for me and i am certain about this however i am unsure why this company is reporting me as late in certain months which should not be the case according to usc 1666b any billing error should be corrected or they will be liable to pay me 100000 for each account reporting inaccurately i never miss a payment i am certain of this i dont get why this company is marking me late for some months usc 1666b states that billing errors should be corrected and shown as paid on time i purchased a xxxx xxxx xxxx xxxx on xxxxxxxx using my td bank xxxx xxxx credit account phone was supposed to be delivered xxxxxxxx instead i get a delivery delayed notice i contact xx
# [{'label': 'NEGATIVE', 'score': 0.9947984218597412}]