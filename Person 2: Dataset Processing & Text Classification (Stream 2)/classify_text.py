from transformers import pipeline

# Initialize the classifier
classifier = pipeline('text-classification', device=0)
# Use the classifier
result = classifier("I love using GPUs for deep learning!")
print(result)

# Test classification with a simple text
test_text = "I love using Hugging Face models!"
results = classifier(test_text)

# Print results
print(results)

# from transformers import pipeline

# # Initialize the classifier
# classifier = pipeline('text-classification')

# try:
#     # Load transcribed text
#     with open('transcribed_text.txt', 'r') as file:
#         transcribed_text = file.read()

#     # Classify the text
#     results = classifier(transcribed_text)

#     # Print results
#     print(results)

# except FileNotFoundError:
#     print("The file 'transcribed_text.txt' was not found.")

# except Exception as e:
#     print(f"An error occurred: {e}")

