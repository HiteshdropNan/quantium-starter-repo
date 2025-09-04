# Soul Foods Pink Morsel Sales Analysis

This project analyzes the impact of a price increase on Pink Morsel sales for Soul Foods.

## Files

- `process_data.py` - Processes the raw CSV data and creates formatted output
- `dash_app.py` - Dash web application for visualizing the sales data
- `formatted_data.csv` - Processed sales data (Sales, Date, Region)
- `requirements.txt` - Python dependencies

## Setup and Running

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

4. Open your browser to `http://127.0.0.1:8050` to view the visualization

## Analysis

The visualization shows Pink Morsel sales over time with a vertical line marking the price increase on January 15th, 2021. This helps answer the business question: "Were sales higher before or after the Pink Morsel price increase?"