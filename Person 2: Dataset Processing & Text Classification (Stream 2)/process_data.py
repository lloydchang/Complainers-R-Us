import pandas as pd
import csv

# Load the dataset
df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# Print column names and the first few rows
print("Columns in dataset:", df.columns)
print("First few rows:")
print(df.head())

# Set display options to show all rows
pd.set_option('display.max_rows', None)

# Extract text from the '_source' column
df['text'] = df['_source'].apply(lambda x: x.get('complaint_what_happened', '') if isinstance(x, dict) else '')

# Clean the text data: remove punctuation and replace newlines with spaces
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)
df['text'] = df['text'].str.replace(r'\s+', ' ', regex=True)  # Replace multiple spaces with a single space

# Add '_id' and 'complaint_id' columns if they do not exist
df['_id'] = df.get('_id', 'NA')
df['complaint_id'] = df['_source'].apply(lambda x: x.get('complaint_id', 'NA') if isinstance(x, dict) else 'NA')

# Create 'cleaned_text' with '_id', 'complaint_id', and 'text'
df['cleaned_text'] = df.apply(
    lambda row: f"{row['_id']}|{row['complaint_id']}|{row['text']}", axis=1
)

# Save cleaned data with identifiers
df[['cleaned_text']].to_csv('cleaned_text.txt', index=False, header=False, quoting=csv.QUOTE_NONE)

print("Text data with identifiers has been cleaned and saved.")
