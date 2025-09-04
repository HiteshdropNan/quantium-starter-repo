import pytest
import sys
import os
import pandas as pd
import re

# Add the current directory to the path so we can import dash_app
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Try to import dash_app, but handle the case where dependencies aren't installed
dash_app = None
dash_app_source = None

try:
    import dash_app
except ImportError as e:
    print(f"Info: Could not import dash_app module (dependencies may not be installed): {e}")
    # Read the source code instead for static analysis
    try:
        with open('dash_app.py', 'r', encoding='utf-8') as f:
            dash_app_source = f.read()
    except FileNotFoundError:
        print("Error: dash_app.py file not found")
        dash_app_source = None


class TestDashApp:
    """Test suite for the Soul Foods Pink Morsel Sales Analysis Dash app."""

    def test_data_file_exists(self):
        """Test that the required data file exists."""
        assert os.path.exists("formatted_data.csv"), "formatted_data.csv should exist"
        
        # Test that the data can be loaded
        df = pd.read_csv("formatted_data.csv")
        assert len(df) > 0, "Data file should contain records"
        assert "Sales" in df.columns, "Data should have Sales column"
        assert "Date" in df.columns, "Data should have Date column"
        assert "Region" in df.columns, "Data should have Region column"
        
        print("✅ Data file test passed: formatted_data.csv exists and has correct structure")

    def test_app_structure_exists(self):
        """Test that the dash_app file exists and has required structure."""
        assert os.path.exists("dash_app.py"), "dash_app.py file should exist"
        
        if dash_app is not None:
            assert hasattr(dash_app, 'app'), "dash_app should have an 'app' attribute"
            assert hasattr(dash_app, 'df'), "dash_app should have a 'df' attribute for data"
            print("✅ App structure test passed: dash_app module imports correctly")
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert 'app = dash.Dash(' in dash_app_source, "Source should create a Dash app"
            assert 'df = pd.read_csv(' in dash_app_source, "Source should load data into df"
            print("✅ App structure test passed: dash_app.py has correct structure (static analysis)")
        else:
            pytest.fail("Could not analyze dash_app structure")

    def test_header_is_present(self):
        """Test that the main header is present in the app layout."""
        if dash_app is not None:
            # Dynamic analysis if module is available
            layout = dash_app.app.layout
            assert layout is not None, "App should have a layout"
            
            # Search for H1 elements in the layout
            def find_h1_elements(component):
                """Recursively find H1 elements in the layout."""
                h1_elements = []
                
                if hasattr(component, 'tag') and component.tag == 'h1':
                    h1_elements.append(component)
                elif hasattr(component, 'children'):
                    if isinstance(component.children, list):
                        for child in component.children:
                            h1_elements.extend(find_h1_elements(child))
                    elif component.children is not None:
                        h1_elements.extend(find_h1_elements(component.children))
                
                return h1_elements
            
            h1_elements = find_h1_elements(layout)
            assert len(h1_elements) > 0, "Layout should contain at least one H1 header element"
            
            # Check if the main header text is present
            header_found = False
            for h1 in h1_elements:
                if hasattr(h1, 'children') and "Soul Foods Pink Morsel Sales Analysis" in str(h1.children):
                    header_found = True
                    break
            
            assert header_found, "Main header 'Soul Foods Pink Morsel Sales Analysis' should be present"
            print("✅ Header test passed: Main header is present in the layout")
            
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert 'html.H1(' in dash_app_source, "Source should contain an H1 element"
            assert 'Soul Foods Pink Morsel Sales Analysis' in dash_app_source, "Source should contain the main header text"
            print("✅ Header test passed: Main header found in source code")
        else:
            pytest.fail("Could not analyze header presence")

    def test_visualization_is_present(self):
        """Test that the sales line chart visualization component is present."""
        if dash_app is not None:
            # Dynamic analysis if module is available
            layout = dash_app.app.layout
            
            # Search for Graph components in the layout
            def find_graph_elements(component):
                """Recursively find Graph elements in the layout."""
                graph_elements = []
                
                if hasattr(component, '__class__') and component.__class__.__name__ == 'Graph':
                    graph_elements.append(component)
                elif hasattr(component, 'children'):
                    if isinstance(component.children, list):
                        for child in component.children:
                            graph_elements.extend(find_graph_elements(child))
                    elif component.children is not None:
                        graph_elements.extend(find_graph_elements(component.children))
                
                return graph_elements
            
            graph_elements = find_graph_elements(layout)
            assert len(graph_elements) > 0, "Layout should contain at least one Graph component"
            
            # Check for the specific sales chart
            sales_chart_found = False
            for graph in graph_elements:
                if hasattr(graph, 'id') and graph.id == 'sales-line-chart':
                    sales_chart_found = True
                    break
            
            assert sales_chart_found, "Sales line chart with id 'sales-line-chart' should be present"
            print("✅ Visualization test passed: Sales line chart component is present")
            
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert 'dcc.Graph(' in dash_app_source, "Source should contain a Graph component"
            assert 'sales-line-chart' in dash_app_source, "Source should contain the sales chart ID"
            assert 'px.line(' in dash_app_source, "Source should create a line chart"
            print("✅ Visualization test passed: Sales line chart found in source code")
        else:
            pytest.fail("Could not analyze visualization presence")

    def test_region_picker_is_present(self):
        """Test that the region filter radio buttons are present."""
        if dash_app is not None:
            # Dynamic analysis if module is available
            layout = dash_app.app.layout
            
            # Search for RadioItems components in the layout
            def find_radio_elements(component):
                """Recursively find RadioItems elements in the layout."""
                radio_elements = []
                
                if hasattr(component, '__class__') and component.__class__.__name__ == 'RadioItems':
                    radio_elements.append(component)
                elif hasattr(component, 'children'):
                    if isinstance(component.children, list):
                        for child in component.children:
                            radio_elements.extend(find_radio_elements(child))
                    elif component.children is not None:
                        radio_elements.extend(find_radio_elements(component.children))
                
                return radio_elements
            
            radio_elements = find_radio_elements(layout)
            assert len(radio_elements) > 0, "Layout should contain at least one RadioItems component"
            
            # Check for the specific region filter
            region_filter_found = False
            for radio in radio_elements:
                if hasattr(radio, 'id') and radio.id == 'region-filter':
                    region_filter_found = True
                    
                    # Check that it has the expected options
                    if hasattr(radio, 'options'):
                        option_values = [opt['value'] for opt in radio.options]
                        expected_values = ['all', 'north', 'south', 'east', 'west']
                        
                        for expected_val in expected_values:
                            assert expected_val in option_values, f"Region filter should have option '{expected_val}'"
                    
                    break
            
            assert region_filter_found, "Region filter with id 'region-filter' should be present"
            print("✅ Region picker test passed: Region filter radio buttons are present with correct options")
            
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert 'dcc.RadioItems(' in dash_app_source, "Source should contain RadioItems component"
            assert 'region-filter' in dash_app_source, "Source should contain the region filter ID"
            
            # Check for all expected region options (check both single and double quotes)
            expected_regions = ['all', 'north', 'south', 'east', 'west']
            for region in expected_regions:
                region_found = (f"'{region}'" in dash_app_source or 
                               f'"{region}"' in dash_app_source or
                               f'value": "{region}"' in dash_app_source)
                assert region_found, f"Source should contain region option '{region}'"
            
            print("✅ Region picker test passed: Region filter radio buttons found in source code")
        else:
            pytest.fail("Could not analyze region picker presence")

    def test_callback_function_exists(self):
        """Test that the callback function for updating the chart exists."""
        if dash_app is not None:
            # Dynamic analysis if module is available
            assert hasattr(dash_app, 'update_chart'), "dash_app should have an 'update_chart' callback function"
            
            # Test that the function can be called with valid inputs
            try:
                result = dash_app.update_chart('all')
                assert result is not None, "update_chart should return a figure"
                print("✅ Callback test passed: update_chart function exists and can be called")
            except Exception as e:
                pytest.fail(f"update_chart function should work with valid input: {e}")
                
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert '@callback' in dash_app_source or '@app.callback' in dash_app_source, "Source should contain callback decorator"
            assert 'def update_chart(' in dash_app_source, "Source should contain update_chart function"
            assert 'Output(' in dash_app_source, "Source should define callback outputs"
            assert 'Input(' in dash_app_source, "Source should define callback inputs"
            print("✅ Callback test passed: Callback function found in source code")
        else:
            pytest.fail("Could not analyze callback function")

    def test_app_configuration(self):
        """Test basic app configuration and setup."""
        if dash_app is not None:
            # Dynamic analysis if module is available
            app = dash_app.app
            
            # Test that the app has a layout
            assert app.layout is not None, "App should have a layout defined"
            
            # Test that data is loaded
            assert dash_app.df is not None, "App should have data loaded"
            assert len(dash_app.df) > 0, "Data should not be empty"
            
            # Test that required columns exist in data
            required_columns = ['Sales', 'Date', 'Region']
            for col in required_columns:
                assert col in dash_app.df.columns, f"Data should have '{col}' column"
            
            print("✅ App configuration test passed: App is properly configured with data and layout")
            
        elif dash_app_source is not None:
            # Static analysis of the source code
            assert 'app.layout =' in dash_app_source, "Source should define app layout"
            assert 'pd.read_csv(' in dash_app_source, "Source should load CSV data"
            assert 'pd.to_datetime(' in dash_app_source, "Source should convert date column"
            print("✅ App configuration test passed: App configuration found in source code")
        else:
            pytest.fail("Could not analyze app configuration")


def run_all_tests():
    """Run all tests and provide a summary."""
    print("🧪 Running Soul Foods Dash App Test Suite")
    print("=" * 50)
    
    test_class = TestDashApp()
    tests = [
        ('Data File Exists', test_class.test_data_file_exists),
        ('App Structure', test_class.test_app_structure_exists),
        ('Header Present', test_class.test_header_is_present),
        ('Visualization Present', test_class.test_visualization_is_present),
        ('Region Picker Present', test_class.test_region_picker_is_present),
        ('Callback Function', test_class.test_callback_function_exists),
        ('App Configuration', test_class.test_app_configuration),
    ]
    
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
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All tests passed! Your Dash app is working correctly!")
        return True
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--summary":
        success = run_all_tests()
        sys.exit(0 if success else 1)
    else:
        # Run with pytest
        pytest.main([__file__, "-v"])