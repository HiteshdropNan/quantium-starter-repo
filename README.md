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
- `test_dash_app.py` - Comprehensive test suite for the Dash application
- `run_tests.py` - Test runner script with multiple execution methods
- `pytest.ini` - Pytest configuration file
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

4. Run the test suite (optional but recommended):
```bash
python run_tests.py
# or
python -m pytest test_dash_app.py -v
```

5. Open your browser to `http://127.0.0.1:8050` to view the interactive visualization

## Key Findings 📈

The analysis reveals consistent sales increases across all regions after the January 15th, 2021 price increase:

- **All Regions Combined**: +35.8% increase
- **North Region**: +36.0% increase  
- **South Region**: +35.6% increase
- **East Region**: +35.3% increase
- **West Region**: +36.4% increase

## Business Impact 💼

**Answer**: Sales were significantly higher AFTER the Pink Morsel price increase, demonstrating the success of Soul Foods' pricing strategy across all geographic markets.

## Testing 🧪

The project includes a comprehensive test suite that verifies:

- **Header Presence**: Ensures the main title is displayed correctly
- **Visualization Presence**: Confirms the sales line chart is properly configured
- **Region Picker Presence**: Validates all region filter options are available
- **Data Integrity**: Checks that data files exist and have correct structure
- **App Configuration**: Verifies proper setup of callbacks and layout
- **Callback Functionality**: Tests that interactive filtering works correctly

### Running Tests

```bash
# Run all tests with detailed output
python run_tests.py

# Run with pytest (if dependencies are installed)
python -m pytest test_dash_app.py -v

# Run individual test summary
python test_dash_app.py --summary
```

The test suite works both with and without Dash dependencies installed, using static code analysis as a fallback when dynamic testing isn't possible.

## Continuous Integration 🔄

The project includes comprehensive CI scripts for automated testing:

### CI Scripts

- **`ci_test.sh`** - Bash script for Unix-like systems (Linux/macOS)
- **`ci_test.bat`** - Batch script for Windows systems
- **`.github/workflows/ci.yml`** - GitHub Actions workflow for cloud CI/CD
- **`test_simple.py`** - Lightweight test suite for CI environments
- **`Makefile`** - Make commands for easy development workflow

### CI Features

- **Virtual Environment Management**: Automatically creates and activates virtual environments
- **Dependency Installation**: Installs required packages from requirements.txt
- **Multi-tier Testing**: Runs simple tests first, then advanced tests if dependencies allow
- **Robust Error Handling**: Multiple fallback test methods for different environments
- **Exit Code Management**: Returns 0 for success, 1 for failure (CI/CD compatible)
- **Cross-platform Support**: Works on Windows, Linux, and macOS

### Running CI Locally

```bash
# Unix-like systems (Linux/macOS)
chmod +x ci_test.sh
./ci_test.sh

# Windows
ci_test.bat

# Using Make (if available)
make ci

# Manual steps
make setup  # Set up environment
make test   # Run tests
```

The CI pipeline ensures code quality and functionality before deployment, making it safe to integrate changes into the main branch.