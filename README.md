# Soul Foods Pink Morsel Sales Analysis 📊

This project analyzes the impact of a price increase on Pink Morsel sales for Soul Foods with an interactive, visually appealing dashboard.

## Features ✨

- **Interactive Region Filtering**: Radio buttons to filter data by North, South, East, West, or All regions
- **Beautiful UI**: Modern gradient design with custom CSS styling and emojis
- **Price Impact Visualization**: Clear vertical line marking the price increase on January 15th, 2021
- **Responsive Charts**: Dynamic color coding for different regions with smooth hover effects
- **Data Insights**: Shows 35.8% average sales increase after price change across all regions

## Files 📁

- `process_data.py` - Processes the raw CSV data and creates formatted output
- `dash_app.py` - Interactive Dash web application with region filtering and custom styling
- `formatted_data.csv` - Processed sales data (Sales, Date, Region)
- `test_visualization.py` - Validation script with region-specific analysis
- `requirements.txt` - Python dependencies

## Setup and Running 🚀

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Process the data (if needed):
```bash
python process_data.py
```

3. Run the Dash app:
```bash
python dash_app.py
```

4. Open your browser to `http://127.0.0.1:8050` to view the interactive visualization

## Key Findings 📈

The analysis reveals consistent sales increases across all regions after the January 15th, 2021 price increase:

- **All Regions Combined**: +35.8% increase
- **North Region**: +36.0% increase  
- **South Region**: +35.6% increase
- **East Region**: +35.3% increase
- **West Region**: +36.4% increase

## Business Impact 💼

**Answer**: Sales were significantly higher AFTER the Pink Morsel price increase, demonstrating the success of Soul Foods' pricing strategy across all geographic markets.