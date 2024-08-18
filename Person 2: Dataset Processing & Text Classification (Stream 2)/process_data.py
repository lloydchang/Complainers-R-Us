#process_data.py

import pandas as pd
import json

# Load the dataset
df = pd.read_json('./ruby_hackathon_data.json')  # Replace with your file path

# Print column names and the first few rows
print("Columns in dataset:", df.columns)
print("First few rows:")
print(df.head())

# Add '_id' and 'complaint_id' columns if they do not exist
df['_id'] = df.get('_id', 'NA')
df['complaint_id'] = df['_source'].apply(lambda x: x.get('complaint_id', 'NA') if isinstance(x, dict) else 'NA')

# Create JSONL file with all data fields
with open('cleaned_text.jsonl', 'w') as f:
    for _, row in df.iterrows():
        json_record = {
            '_id': row['_id'],
            'complaint_id': row['complaint_id'],
            'product': row['_source'].get('product', ''),
            'complaint_what_happened': row['_source'].get('complaint_what_happened', ''),
            'date_sent_to_company': row['_source'].get('date_sent_to_company', ''),
            'issue': row['_source'].get('issue', ''),
            'sub_product': row['_source'].get('sub_product', ''),
            'zip_code': row['_source'].get('zip_code', ''),
            'tags': row['_source'].get('tags', ''),
            'timely': row['_source'].get('timely', ''),
            'consumer_consent_provided': row['_source'].get('consumer_consent_provided', ''),
            'company_response': row['_source'].get('company_response', ''),
            'submitted_via': row['_source'].get('submitted_via', ''),
            'company': row['_source'].get('company', ''),
            'date_received': row['_source'].get('date_received', ''),
            'state': row['_source'].get('state', ''),
            'consumer_disputed': row['_source'].get('consumer_disputed', ''),
            'company_public_response': row['_source'].get('company_public_response', ''),
            'sub_issue': row['_source'].get('sub_issue', ''),
            'text': row['_source'].get('complaint_what_happened', '')  # Adding cleaned text
        }
        f.write(json.dumps(json_record) + '\n')

print("Data with all fields has been cleaned and saved.")
