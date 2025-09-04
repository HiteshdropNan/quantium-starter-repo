#!/usr/bin/env python3
"""
Test runner script for the Soul Foods Dash app test suite.
This script runs all tests and provides a summary of results.
"""

import subprocess
import sys
import os

def run_tests_with_pytest():
    """Run the test suite using pytest."""
    try:
        # Run pytest with verbose output
        result = subprocess.run([
            sys.executable, "-m", "pytest", 
            "test_dash_app.py", 
            "-v", 
            "--tb=short"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:")
            print(result.stderr)
        
        return result.returncode == 0
            
    except FileNotFoundError:
        print("❌ Error: pytest not found. Falling back to direct test execution...")
        return False
    except Exception as e:
        print(f"❌ Error running pytest: {e}")
        return False

def run_tests_directly():
    """Run tests directly without pytest."""
    try:
        # Import and run the test summary
        result = subprocess.run([
            sys.executable, "test_dash_app.py", "--summary"
        ], capture_output=True, text=True)
        
        print(result.stdout)
        if result.stderr:
            print("Warnings/Errors:")
            print(result.stderr)
        
        return result.returncode == 0
        
    except Exception as e:
        print(f"❌ Error running tests directly: {e}")
        return False

def main():
    """Main test runner function."""
    print("🧪 Running Soul Foods Dash App Test Suite")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("dash_app.py"):
        print("❌ Error: dash_app.py not found. Please run this script from the project root directory.")
        return False
    
    if not os.path.exists("formatted_data.csv"):
        print("❌ Error: formatted_data.csv not found. Please run process_data.py first.")
        return False
    
    # Try pytest first, fall back to direct execution
    success = run_tests_with_pytest()
    
    if not success:
        print("\n🔄 Trying alternative test execution method...")
        success = run_tests_directly()
    
    if success:
        print("\n✅ All tests passed successfully!")
        print("🎉 Your Dash app is working correctly!")
    else:
        print("\n❌ Some tests failed.")
        print("Please check the output above for details.")
    
    return success

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)