import pandas as pd
import os

# Read all three CSV files
data_files = ['data/daily_sales_data_0.csv', 'data/daily_sales_data_1.csv', 'data/daily_sales_data_2.csv']
all_data = []

for file in data_files:
    df = pd.read_csv(file)
    all_data.append(df)

# Combine all dataframes
combined_df = pd.concat(all_data, ignore_index=True)

# Filter for Pink Morsels only
pink_morsels = combined_df[combined_df['product'] == 'pink morsel'].copy()

# Remove dollar sign from price and convert to float
pink_morsels['price'] = pink_morsels['price'].str.replace('$', '', regex=False).astype(float)

# Calculate sales (price * quantity)
pink_morsels['sales'] = pink_morsels['price'] * pink_morsels['quantity']

# Select only the required columns and rename to match specification
output_df = pink_morsels[['sales', 'date', 'region']].copy()
output_df = output_df.rename(columns={'sales': 'Sales', 'date': 'Date', 'region': 'Region'})

# Save to output file
output_df.to_csv('formatted_data.csv', index=False)

print(f"Processed {len(output_df)} Pink Morsel records")
print(f"Output saved to formatted_data.csv")
print("\nFirst few rows of output:")
print(output_df.head())