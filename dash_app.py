import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd
from datetime import datetime

# Load the processed data
df = pd.read_csv('formatted_data.csv')

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create the Dash app
app = dash.Dash(__name__)

# Define custom CSS styles
app.layout = html.Div([
    # Header section with gradient background
    html.Div([
        html.H1("Soul Foods Pink Morsel Sales Analysis", 
                style={
                    'textAlign': 'center', 
                    'marginBottom': '10px', 
                    'color': 'white',
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '2.5rem',
                    'fontWeight': 'bold',
                    'textShadow': '2px 2px 4px rgba(0,0,0,0.3)'
                }),
        
        html.P("Impact of Price Increase on January 15th, 2021", 
               style={
                   'textAlign': 'center', 
                   'fontSize': '1.2rem', 
                   'color': '#f8f9fa',
                   'fontFamily': 'Arial, sans-serif',
                   'marginBottom': '0px',
                   'fontStyle': 'italic'
               })
    ], style={
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'padding': '40px 20px',
        'marginBottom': '30px',
        'borderRadius': '0 0 20px 20px',
        'boxShadow': '0 4px 15px rgba(0,0,0,0.2)'
    }),
    
    # Control panel
    html.Div([
        html.Div([
            html.H3("Filter by Region", 
                    style={
                        'color': '#2c3e50',
                        'fontFamily': 'Arial, sans-serif',
                        'marginBottom': '15px',
                        'fontSize': '1.3rem'
                    }),
            
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': '🌍 All Regions', 'value': 'all'},
                    {'label': '⬆️ North', 'value': 'north'},
                    {'label': '⬇️ South', 'value': 'south'},
                    {'label': '➡️ East', 'value': 'east'},
                    {'label': '⬅️ West', 'value': 'west'}
                ],
                value='all',
                style={
                    'fontFamily': 'Arial, sans-serif',
                    'fontSize': '1.1rem'
                },
                inputStyle={
                    'marginRight': '8px',
                    'transform': 'scale(1.2)'
                },
                labelStyle={
                    'display': 'block',
                    'marginBottom': '10px',
                    'padding': '8px 15px',
                    'backgroundColor': '#f8f9fa',
                    'borderRadius': '8px',
                    'border': '2px solid #e9ecef',
                    'cursor': 'pointer',
                    'transition': 'all 0.3s ease'
                }
            )
        ], style={
            'backgroundColor': 'white',
            'padding': '25px',
            'borderRadius': '15px',
            'boxShadow': '0 4px 15px rgba(0,0,0,0.1)',
            'border': '1px solid #e9ecef'
        })
    ], style={
        'width': '300px',
        'margin': '0 auto 30px auto'
    }),
    
    # Chart container
    html.Div([
        dcc.Graph(
            id='sales-line-chart',
            style={'height': '600px'}
        )
    ], style={
        'backgroundColor': 'white',
        'padding': '25px',
        'borderRadius': '15px',
        'boxShadow': '0 4px 15px rgba(0,0,0,0.1)',
        'border': '1px solid #e9ecef',
        'margin': '0 20px'
    }),
    
    # Footer
    html.Div([
        html.P("📊 Data-driven insights for better business decisions", 
               style={
                   'textAlign': 'center',
                   'color': '#6c757d',
                   'fontFamily': 'Arial, sans-serif',
                   'fontSize': '0.9rem',
                   'fontStyle': 'italic'
               })
    ], style={
        'marginTop': '30px',
        'padding': '20px'
    })
    
], style={
    'backgroundColor': '#f8f9fa',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif'
})

# Callback for updating the chart based on region selection
@callback(
    Output('sales-line-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selected region
    if selected_region == 'all':
        # Group by date and sum sales across all regions
        filtered_data = df.groupby('Date')['Sales'].sum().reset_index()
        chart_title = 'Pink Morsel Daily Sales - All Regions'
        line_color = '#667eea'
    else:
        # Filter for specific region and group by date
        region_data = df[df['Region'] == selected_region]
        filtered_data = region_data.groupby('Date')['Sales'].sum().reset_index()
        chart_title = f'Pink Morsel Daily Sales - {selected_region.title()} Region'
        
        # Different colors for different regions
        color_map = {
            'north': '#e74c3c',
            'south': '#f39c12', 
            'east': '#27ae60',
            'west': '#9b59b6'
        }
        line_color = color_map.get(selected_region, '#667eea')
    
    # Sort by date
    filtered_data = filtered_data.sort_values('Date')
    
    # Create the line chart
    fig = px.line(
        filtered_data, 
        x='Date', 
        y='Sales',
        title=chart_title,
        labels={
            'Date': 'Date',
            'Sales': 'Total Daily Sales ($)'
        }
    )
    
    # Update layout and styling
    fig.update_traces(
        line=dict(color=line_color, width=3),
        hovertemplate='<b>Date:</b> %{x}<br><b>Sales:</b> $%{y:,.0f}<extra></extra>'
    )
    
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Total Daily Sales ($)",
        hovermode='x unified',
        plot_bgcolor='white',
        paper_bgcolor='white',
        title={
            'text': chart_title,
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 20, 'color': '#2c3e50', 'family': 'Arial, sans-serif'}
        },
        xaxis=dict(
            gridcolor='#e9ecef',
            linecolor='#dee2e6'
        ),
        yaxis=dict(
            gridcolor='#e9ecef',
            linecolor='#dee2e6'
        ),
        margin=dict(l=60, r=60, t=80, b=60)
    )
    
    # Add vertical line for price increase
    fig.add_vline(
        x=datetime(2021, 1, 15), 
        line_dash="dash", 
        line_color="#e74c3c",
        line_width=2,
        annotation_text="💰 Price Increase<br>Jan 15, 2021",
        annotation_position="top",
        annotation=dict(
            font=dict(color="#e74c3c", size=12),
            bgcolor="rgba(231, 76, 60, 0.1)",
            bordercolor="#e74c3c",
            borderwidth=1
        )
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)