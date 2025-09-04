#!/usr/bin/env python3
"""
Simple test suite for CI that doesn't require heavy dependencies.
This test focuses on basic file structure and code syntax validation.
"""

import os
import sys
import ast
import re


def test_required_files_exist():
    """Test that all required files exist."""
    required_files = [
        'dash_app.py',
        'process_data.py',
        'formatted_data.csv',
        'requirements.txt'
    ]
    
    for file in required_files:
        assert os.path.exists(file), f"Required file '{file}' not found"
    
    print("✅ All required files exist")


def test_python_syntax():
    """Test that Python files have valid syntax."""
    python_files = [
        'dash_app.py',
        'process_data.py',
        'test_dash_app.py',
        'run_tests.py'
    ]
    
    for file in python_files:
        if os.path.exists(file):
            with open(file, 'r', encoding='utf-8') as f:
                try:
                    ast.parse(f.read())
                    print(f"✅ {file} has valid Python syntax")
                except SyntaxError as e:
                    raise AssertionError(f"Syntax error in {file}: {e}")


def test_dash_app_structure():
    """Test that dash_app.py has the required structure."""
    with open('dash_app.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for required imports
    assert 'import dash' in content, "dash_app.py should import dash"
    assert 'import pandas' in content, "dash_app.py should import pandas"
    assert 'import plotly' in content, "dash_app.py should import plotly"
    
    # Check for required components
    assert 'app = dash.Dash(' in content, "dash_app.py should create a Dash app"
    assert 'html.H1(' in content, "dash_app.py should have an H1 header"
    assert 'dcc.Graph(' in content, "dash_app.py should have a Graph component"
    assert 'dcc.RadioItems(' in content, "dash_app.py should have RadioItems"
    assert '@callback' in content or '@app.callback' in content, "dash_app.py should have callbacks"
    
    # Check for specific text content
    assert 'Soul Foods Pink Morsel Sales Analysis' in content, "Header text should be present"
    assert 'sales-line-chart' in content, "Chart ID should be present"
    assert 'region-filter' in content, "Region filter ID should be present"
    
    print("✅ dash_app.py has correct structure")


def test_data_file_structure():
    """Test that the data file has the correct structure."""
    with open('formatted_data.csv', 'r', encoding='utf-8') as f:
        first_line = f.readline().strip()
    
    expected_headers = ['Sales', 'Date', 'Region']
    actual_headers = first_line.split(',')
    
    for header in expected_headers:
        assert header in actual_headers, f"Data file should have '{header}' column"
    
    print("✅ Data file has correct structure")


def test_requirements_file():
    """Test that requirements.txt has necessary dependencies."""
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        content = f.read().lower()
    
    required_packages = ['dash', 'pandas', 'plotly', 'pytest']
    
    for package in required_packages:
        assert package in content, f"requirements.txt should include '{package}'"
    
    print("✅ requirements.txt has necessary dependencies")


def run_all_tests():
    """Run all tests and return success status."""
    tests = [
        ('Required Files Exist', test_required_files_exist),
        ('Python Syntax Valid', test_python_syntax),
        ('Dash App Structure', test_dash_app_structure),
        ('Data File Structure', test_data_file_structure),
        ('Requirements File', test_requirements_file),
    ]
    
    print("🧪 Running Simple CI Test Suite")
    print("=" * 40)
    
    passed = 0
    failed = 0
    
    for test_name, test_func in tests:
        try:
            print(f"\n🔍 Running: {test_name}")
            test_func()
            passed += 1
        except Exception as e:
            print(f"❌ FAILED: {test_name} - {e}")
            failed += 1
    
    print("\n" + "=" * 40)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! CI pipeline successful!")
        return True
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)