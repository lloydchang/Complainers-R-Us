from transformers import pipeline

# Initialize the classifier
classifier = pipeline('text-classification', device=0)
# Use the classifier
test_text = "I love using GPUs for deep learning!"
result = classifier(test_text)
print ("\n")
print (test_text)
print(result)

# Test classification with a simple text
test_text = "I love using Hugging Face models!"
results = classifier(test_text)
print ("\n")
print (test_text)
print(result)
print ("\n")

transcribed_text = "cleaned_text.txt"

try:
    # Load transcribed text
    with open(transcribed_text, 'r') as file:
        transcribed_text = file.read()

    # Classify the text
    results = classifier(transcribed_text)

    # Print results
    print(results)

except FileNotFoundError:
    print("The file " + transcribed_text + "was not found.")

except Exception as e:
    print(f"An error occurred: {e}")

# Token indices sequence length is longer than the specified maximum sequence length for this model (944055 > 512). Running this sequence through the model will result in indexing errors
# An error occurred: The size of tensor a (944055) must match the size of tensor b (512) at non-singleton dimension 1
