import pandas as pd

# Load processed CSV
data = pd.read_csv('../data/processed/sessions_preprocessed.csv')

window_size = 5
sequences = []

for i in range(len(data) - window_size + 1):
    window = data.iloc[i:i+window_size]
    # Convert each window into a list of observations
    sequences.append(window[['req_rate', 'recon_ratio', 'exploit_ratio', 'persistence_flag']].values.tolist())

# Example: save sequences as CSV or JSON
import json
with open('../data/processed/session_sequences.json', 'w') as f:
    json.dump(sequences, f)
