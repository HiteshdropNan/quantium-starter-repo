import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from datetime import datetime

# Load the processed data
df = pd.read_csv('formatted_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Group by date and sum sales across all regions for daily totals
daily_sales = df.groupby('Date')['Sales'].sum().reset_index()

# Sort by date to ensure proper line chart ordering
daily_sales = daily_sales.sort_values('Date')

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Analysis", 
            style={'textAlign': 'center', 'marginBottom': 30, 'color': '#2c3e50'}),
    
    html.Div([
        html.P("Impact of Price Increase on January 15th, 2021", 
               style={'textAlign': 'center', 'fontSize': 18, 'color': '#7f8c8d', 'marginBottom': 30})
    ]),
    
    dcc.Graph(
        id='sales-line-chart',
        figure=px.line(
            daily_sales, 
            x='Date', 
            y='Sales',
            title='Pink Morsel Daily Sales Over Time',
            labels={
                'Date': 'Date',
                'Sales': 'Total Daily Sales ($)'
            }
        ).update_layout(
            xaxis_title="Date",
            yaxis_title="Total Daily Sales ($)",
            hovermode='x unified',
            plot_bgcolor='white',
            paper_bgcolor='white'
        ).add_vline(
            x=datetime(2021, 1, 15), 
            line_dash="dash", 
            line_color="red",
            annotation_text="Price Increase<br>Jan 15, 2021",
            annotation_position="top"
        )
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)