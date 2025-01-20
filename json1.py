# import json
# import pandas as pd
# from tkinter import Tk, filedialog

# # Function to prompt user for file selection
# def select_files():
#     Tk().withdraw()  # Hide the root Tkinter window
#     file_paths = filedialog.askopenfilenames(
#         title="Select JSON Files",
#         filetypes=[("JSON Files", "*.json")]
#     )
#     return file_paths

# # Main code
# file_paths = select_files()
# if not file_paths:
#     print("No files selected. Exiting.")
# else:
#     results = []
#     for file_path in file_paths:
#         with open(file_path, 'r') as file:
#             data = json.load(file)
#             results.extend([
#                 {"File Name": file_path.split('/')[-1], "Net Price": entry.get("net_price", "").strip()}
#                 for entry in data
#             ])

#     # Convert to DataFrame
#     df = pd.DataFrame(results)

#     # Save to Excel
#     output_path = "output_net_price.xlsx"
#     df.to_excel(output_path, index=False)

#     print(f"Data has been extracted and saved to {output_path}")


# import json

# # Define the keys to extract
# target_keys = [
#     "BE no", "BE date", "Port Entry", "GSTIN/TYPE", "CB Code", "Importer", "Total Ass Val",
#     "IGST", "BCD", "ACD", "Total Amount", "Amount", "Invoice NO", "INV.AMT", "Inv Date",
#     "Buyers Name", "Suppliers Name", "Line Items", "Supporting Doc"
# ]

# # Load the JSON file with utf-8 encoding
# def load_json(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         return json.load(f)


# # Extract key-value pairs from the JSON data
# def extract_key_values(data, keys):
#     extracted_data = {}
    
#     def recursive_extract(d):
#         if isinstance(d, dict):
#             for key, value in d.items():
#                 if key in keys:
#                     extracted_data[key] = value
#                 recursive_extract(value)
#         elif isinstance(d, list):
#             for item in d:
#                 recursive_extract(item)

#     recursive_extract(data)
#     return extracted_data

# # Main execution
# if __name__ == "__main__":
#     # Path to the JSON file (replace with your file path)
#     json_file_path = "3433168.pdf 1.json"

#     # Load the JSON data
#     json_data = load_json(json_file_path)

#     # Extract the relevant data
#     extracted_data = extract_key_values(json_data, target_keys)

#     # Print the extracted data
#     print("Extracted Data:")
#     for key, value in extracted_data.items():
#         print(f"{key}: {value}")



import json

# Function to load JSON from a file with UTF-8 encoding
def load_json_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return {}

# Function to extract relevant fields from JSON data dynamically
def extract_invoice_fields(data):
    # Navigate to the "analyzeResult" section
    analyze_result = data.get("analyzeResult", {})
    content = analyze_result.get("content", "")
    
    # Use dictionaries for key-value extraction based on actual structure
    extracted_data = {}
    
    # Try extracting known fields from the content
    if isinstance(content, str):
        extracted_data["Content"] = content
    
    if isinstance(analyze_result, dict):
        extracted_data.update({
            "Invoice No": analyze_result.get("Invoice No", "Not Found"),
            "Port Code": analyze_result.get("Port Code", "Not Found"),
            "Country of Origin": analyze_result.get("Country of Origin", "Not Found"),
            "Country of Consignment": analyze_result.get("Country of Consignment", "Not Found"),
            "Gross Weight": analyze_result.get("G.WT (KGS)", "Not Found"),
            "Invoice Date": analyze_result.get("BE Date", "Not Found"),
            "Buyer Name & Address": analyze_result.get("Buyer's Name & Address", "Not Found"),
            "Seller Name & Address": analyze_result.get("Seller's Name & Address", "Not Found")
        })
    
    return extracted_data

# Function to dynamically print all keys for inspection
def inspect_keys(data, prefix=""):
    if isinstance(data, dict):
        for key, value in data.items():
            print(f"{prefix}{key}")
            inspect_keys(value, prefix=prefix + "  ")
    elif isinstance(data, list):
        for index, item in enumerate(data):
            print(f"{prefix}[{index}]")
            inspect_keys(item, prefix=prefix + "  ")

# Example usage
if __name__ == "__main__":
    file_path = r"C:\Users\Meet\Desktop\Net_Price\env\3433168.pdf 1.json"  # Replace with the actual file path
    
    # Load data from file
    data = load_json_from_file(file_path)
    
    # Inspect keys if needed
    print("JSON Structure:")
    inspect_keys(data)
    
    # Extract the required fields
    invoice_fields = extract_invoice_fields(data)
    
    # Print extracted fields
    print("\nExtracted Fields:")
    for key, value in invoice_fields.items():
        print(f"{key}: {value}")
