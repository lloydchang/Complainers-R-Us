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

# Extract text from the '_source' column
df['text'] = df['_source'].apply(lambda x: x.get('complaint_what_happened', '') if isinstance(x, dict) else '')

# Clean the text data
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
df['text'].to_csv('cleaned_text.txt', index=False, header=False)

print("Text data has been cleaned and saved.")
