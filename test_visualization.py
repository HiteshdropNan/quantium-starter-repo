import pandas as pd
from datetime import datetime

# Test the data processing for the visualization
print("Testing visualization data processing...")

# Load the processed data
df = pd.read_csv('formatted_data.csv')
print(f"Loaded {len(df)} records")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and sum sales across all regions for daily totals
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()
daily_sales = daily_sales.sort_values('Date')

print(f"Processed into {len(daily_sales)} daily totals")
print(f"Date range: {daily_sales['Date'].min()} to {daily_sales['Date'].max()}")

# Check data around the price increase date
price_increase_date = datetime(2021, 1, 15)
before_increase = daily_sales[daily_sales['Date'] < price_increase_date]['Sales'].mean()
after_increase = daily_sales[daily_sales['Date'] >= price_increase_date]['Sales'].mean()

print(f"\nAverage daily sales before Jan 15, 2021: ${before_increase:.2f}")
print(f"Average daily sales after Jan 15, 2021: ${after_increase:.2f}")
print(f"Percentage increase: {((after_increase - before_increase) / before_increase * 100):.1f}%")

print("\nFirst few daily totals:")
print(daily_sales.head())

print("\nLast few daily totals:")
print(daily_sales.tail())