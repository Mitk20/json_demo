import re

# Load the text file
with open("output_key_value_pairs.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Define keys to search for
keys = [
    "Port Code", "BE No", "BE Date", "BE Type", "Invoice No", "Invoice Date",
    "Importer Name & Address", "Country of Origin", "Total Duty", "Item Details"
]

# Initialize dictionary for key-value pairs
extracted_data = {}
current_key = None

# Iterate through lines to extract data
for line in lines:
    line = line.strip()  # Remove whitespace
    if not line:
        continue  # Skip empty lines
    
    # Check if the line matches a key
    for key in keys:
        if line.startswith(key):
            current_key = key
            extracted_data[current_key] = ""
            break
    else:
        # If no key is matched, append the line to the current key's value
        if current_key:
            extracted_data[current_key] += " " + line

# Clean up values
for key in extracted_data:
    extracted_data[key] = extracted_data[key].strip()

# Output the extracted key-value pairs
output_file = "extracted_invoice_data.json"
import json
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(extracted_data, json_file, indent=4)

print(f"Extracted data saved to {output_file}")
