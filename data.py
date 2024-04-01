import pandas as pd

# Try reading the CSV file and handle parsing errors
try:
    facebook_df = pd.read_csv("facebook_dataset.csv")
except pd.errors.ParserError as e:
    print(f"Error reading CSV file: {e}")
    # Handle the error by skipping problematic lines
    facebook_df = pd.read_csv("facebook_dataset.csv", error_bad_lines=False)

# Continue with your data processing logic...


# Step 1: Data Loading
facebook_df = pd.read_csv("facebook_dataset.csv")
google_df = pd.read_csv("google_dataset.csv")
website_df = pd.read_csv("website_dataset.csv")

# Step 2: Data Cleaning
# Assuming cleaning functions are defined here if needed

# Step 3: Column Selection
common_columns = ['Category', 'Address', 'Phone', 'Company Name']
facebook_selected = facebook_df[common_columns].copy()
google_selected = google_df[common_columns].copy()
website_selected = website_df[common_columns].copy()

# Step 4: Data Integration
# Merge datasets using outer join to retain data from all datasets
merged_df = pd.merge(facebook_selected, google_selected, on=common_columns, how='outer')
merged_df = pd.merge(merged_df, website_selected, on=common_columns, how='outer')

# Step 5: Data Export
merged_df.to_csv("merged_dataset.csv", index=False)

# Displaying first few rows of the merged dataset
print(merged_df.head())
