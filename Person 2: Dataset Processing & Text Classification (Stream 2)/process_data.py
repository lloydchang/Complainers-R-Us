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


import pandas as pd

# Load the dataset
df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# print column names and the first few rows
print("Columns in dataset:", df.columns)
print("First few rows:")
print(df.head())

# Set display options to show all rows
pd.set_option('display.max_rows', None)

# Assuming df is your DataFrame
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


# ❯ python process_data.py

# Columns in dataset: Index(['_index', '_type', '_id', '_score', '_source', 'sort'], dtype='object')
# First few rows:
#                 _index _type      _id  _score                                            _source   sort
# 0  complaint-public-v2  _doc  9615747     NaN  {'product': 'Credit card', 'complaint_what_hap...   [33]
# 1  complaint-public-v2  _doc  9005055     NaN  {'product': 'Credit card', 'complaint_what_hap...   [40]
# 2  complaint-public-v2  _doc  9154222     NaN  {'product': 'Credit card', 'complaint_what_hap...  [128]
# 3  complaint-public-v2  _doc  9157176     NaN  {'product': 'Credit card', 'complaint_what_hap...  [203]
# 4  complaint-public-v2  _doc  9628394     NaN  {'product': 'Credit card', 'complaint_what_hap...  [211]
# Columns in dataset: Index(['_index', '_type', '_id', '_score', '_source', 'sort'], dtype='object')
# All rows:
#                    _index _type      _id  _score                                            _source       sort
# 0     complaint-public-v2  _doc  9615747     NaN  {'product': 'Credit card', 'complaint_what_hap...       [33]
# …
# 4407  complaint-public-v2  _doc  9021400     NaN  {'product': 'Credit card', 'complaint_what_hap...  [1028806]
# Traceback (most recent call last):
#   File "/Users/lloyd/.pyenv/versions/3.12.4/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3805, in get_loc
#     return self._engine.get_loc(casted_key)
#            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "index.pyx", line 167, in pandas._libs.index.IndexEngine.get_loc
#   File "index.pyx", line 196, in pandas._libs.index.IndexEngine.get_loc
#   File "pandas/_libs/hashtable_class_helper.pxi", line 7081, in pandas._libs.hashtable.PyObjectHashTable.get_item
#   File "pandas/_libs/hashtable_class_helper.pxi", line 7089, in pandas._libs.hashtable.PyObjectHashTable.get_item
# KeyError: 'text'

# The above exception was the direct cause of the following exception:

# Traceback (most recent call last):
#   File "/Users/lloyd/github/Complainers-R-Us-Org/Complainers-R-Us/Person 2: Dataset Processing & Text Classification (Stream 2)/process_data.py", line 20, in <module>
#     df['text'] = df['text'].str.replace(r'[^\w\s]', '', regex=True)
#                  ~~^^^^^^^^
#   File "/Users/lloyd/.pyenv/versions/3.12.4/lib/python3.12/site-packages/pandas/core/frame.py", line 4102, in __getitem__
#     indexer = self.columns.get_loc(key)
#               ^^^^^^^^^^^^^^^^^^^^^^^^^
#   File "/Users/lloyd/.pyenv/versions/3.12.4/lib/python3.12/site-packages/pandas/core/indexes/base.py", line 3812, in get_loc
#     raise KeyError(key) from err
# KeyError: 'text'


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
