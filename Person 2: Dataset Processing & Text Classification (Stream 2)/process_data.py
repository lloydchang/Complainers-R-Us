# import pandas as pd

# # Load the dataset
# # df = pd.read_csv('path_to_your_downloaded_dataset.csv')  # Replace with your file path
# df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# # Clean the text data
# df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# # Save cleaned text
# df['text'].to_csv('cleaned_text.txt', index=False, header=False)

import pandas as pd

# Load the dataset
# df = pd.read_csv('path_to_your_downloaded_dataset.csv')  # Replace with your file path
df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# Print column names and the first few rows
print("Columns in dataset:", df.columns)
print("First few rows:")
print(df.head())
