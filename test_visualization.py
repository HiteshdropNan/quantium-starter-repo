import pandas as pd
from datetime import datetime

# Test the data processing for the visualization
print("Testing visualization data processing...")

# Load the processed data
df = pd.read_csv('formatted_data.csv')
print(f"Loaded {len(df)} records")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Test region filtering functionality
regions = df['Region'].unique()
print(f"Available regions: {list(regions)}")

print("\n" + "="*50)
print("REGION-SPECIFIC ANALYSIS")
print("="*50)

price_increase_date = datetime(2021, 1, 15)

for region in ['all'] + list(regions):
    if region == 'all':
        region_data = df.groupby('Date')['Sales'].sum().reset_index()
        region_name = "All Regions"
    else:
        filtered_df = df[df['Region'] == region]
        region_data = filtered_df.groupby('Date')['Sales'].sum().reset_index()
        region_name = f"{region.title()} Region"
    
    region_data = region_data.sort_values('Date')
    
    # Calculate before/after price increase
    before_increase = region_data[region_data['Date'] < price_increase_date]['Sales'].mean()
    after_increase = region_data[region_data['Date'] >= price_increase_date]['Sales'].mean()
    
    print(f"\n{region_name}:")
    print(f"  Records: {len(region_data)} daily totals")
    print(f"  Before price increase: ${before_increase:.2f}")
    print(f"  After price increase: ${after_increase:.2f}")
    print(f"  Change: {((after_increase - before_increase) / before_increase * 100):+.1f}%")

print("\n" + "="*50)
print("OVERALL SUMMARY")
print("="*50)

# Group by date and sum sales across all regions for daily totals
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
daily_sales = daily_sales.sort_values('Date')

print(f"Total processed into {len(daily_sales)} daily totals")
print(f"Date range: {daily_sales['Date'].min().strftime('%Y-%m-%d')} to {daily_sales['Date'].max().strftime('%Y-%m-%d')}")

before_increase = daily_sales[daily_sales['Date'] < price_increase_date]['Sales'].mean()
after_increase = daily_sales[daily_sales['Date'] >= price_increase_date]['Sales'].mean()

print(f"\nOverall average daily sales before Jan 15, 2021: ${before_increase:.2f}")
print(f"Overall average daily sales after Jan 15, 2021: ${after_increase:.2f}")
print(f"Overall percentage increase: {((after_increase - before_increase) / before_increase * 100):.1f}%")

print("\nSample data structure:")
print(df.head())