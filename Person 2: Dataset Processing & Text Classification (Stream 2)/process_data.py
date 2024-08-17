import pandas as pd

# Load the dataset
df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# print column names and the first few rows
print("Columns in dataset:", df.columns)
print("First few rows:")
print(df.head())

# Set display options to show all rows
pd.set_option('display.max_rows', None)

# Assuming `df` is your DataFrame
print("Columns in dataset:", df.columns)
print("All rows:")
print(df)

# Clean the text data
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
df['text'].to_csv('cleaned_text.txt', index=False, header=False)

# Clean the text data
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
df['text'].to_csv('cleaned_text.txt', index=False, header=False)
