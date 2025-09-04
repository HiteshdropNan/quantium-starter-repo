# Makefile for Soul Foods Dash App

.PHONY: help install test clean setup ci lint format

# Default target
help:
	@echo "Soul Foods Dash App - Available Commands:"
	@echo "========================================="
	@echo "  setup     - Set up virtual environment and install dependencies"
	@echo "  install   - Install dependencies"
	@echo "  test      - Run the test suite"
	@echo "  ci        - Run CI pipeline (setup + test)"
	@echo "  lint      - Run code linting (if flake8 is installed)"
	@echo "  format    - Format code with black (if black is installed)"
	@echo "  clean     - Clean up generated files and virtual environment"
	@echo "  run       - Run the Dash application"
	@echo "  process   - Process the raw data"

# Set up virtual environment and install dependencies
setup:
	@echo "Setting up virtual environment..."
	python -m venv venv
	@echo "Activating virtual environment and installing dependencies..."
	@if [ -f "venv/bin/activate" ]; then \
		. venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt; \
	elif [ -f "venv/Scripts/activate" ]; then \
		. venv/Scripts/activate && pip install --upgrade pip && pip install -r requirements.txt; \
	else \
		echo "Virtual environment activation failed"; \
		exit 1; \
	fi
	@echo "Setup complete!"

# Install dependencies (assumes virtual environment is activated)
install:
	pip install --upgrade pip
	pip install -r requirements.txt

# Run the test suite
test:
	@echo "Running test suite..."
	@python -m pytest test_dash_app.py -v || python test_dash_app.py --summary || python run_tests.py

# Run full CI pipeline
ci:
	@echo "Running CI pipeline..."
	@if [ -f "ci_test.sh" ]; then \
		chmod +x ci_test.sh && ./ci_test.sh; \
	elif [ -f "ci_test.bat" ]; then \
		./ci_test.bat; \
	else \
		echo "No CI script found, running basic test..."; \
		make test; \
	fi

# Run code linting
lint:
	@echo "Running code linting..."
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics; \
		flake8 . --count --exit-zero --max-complexity=10 --max-line-length=88 --statistics; \
	else \
		echo "flake8 not installed. Install with: pip install flake8"; \
	fi

# Format code
format:
	@echo "Formatting code..."
	@if command -v black >/dev/null 2>&1; then \
		black .; \
	else \
		echo "black not installed. Install with: pip install black"; \
	fi

# Clean up generated files
clean:
	@echo "Cleaning up..."
	rm -rf venv/
	rm -rf __pycache__/
	rm -rf .pytest_cache/
	rm -rf *.pyc
	rm -rf .coverage
	@echo "Cleanup complete!"

# Run the Dash application
run:
	@if [ ! -f "formatted_data.csv" ]; then \
		echo "Data file not found, processing data first..."; \
		python process_data.py; \
	fi
	python dash_app.py

# Process the raw data
process:
	python process_data.py