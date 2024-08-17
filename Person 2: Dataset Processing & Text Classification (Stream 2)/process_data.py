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
# df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
# df['text'].to_csv('cleaned_text.txt', index=False, header=False)

# Clean the text data
# df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
# df['text'].to_csv('cleaned_text.txt', index=False, header=False)

# It looks like the column 'text' does not exist in your DataFrame. According to the error message and the dataset preview, your DataFrame has columns ['_index', '_type', '_id', '_score', '_source', 'sort'].

# The 'text' column that you are trying to access might not be directly available. Instead, the text data appears to be nested inside the _source column.

# Here’s how you can extract and clean the text data from the _source column:

# Extract the text from _source: Assuming that the text is stored in a key named 'complaint_what_happened' inside the _source dictionary.

# Clean and save the text data: After extraction, clean and save it as you intended.

# Here’s the updated code:

# Extract text from the '_source' column
df['text'] = df['_source'].apply(lambda x: x.get('complaint_what_happened', '') if isinstance(x, dict) else '')

# Clean the text data
df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)

# Save cleaned text
df['text'].to_csv('cleaned_text.txt', index=False, header=False)

print("Text data has been cleaned and saved.")
