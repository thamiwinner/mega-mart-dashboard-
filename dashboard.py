import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data for Mega Mart
data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Sales': [20000, 24000, 22000, 28000, 30000, 32000],
    'Customers': [200, 250, 210, 270, 290, 310],
    'Inventory Level': [100, 80, 90, 70, 60, 50]
}

df = pd.DataFrame(data)

# Create visualizations
sales_fig = px.line(df, x='Month', y='Sales', title='Sales Performance Over Time')
customers_fig = px.bar(df, x='Month', y='Customers', title='Customer Demographics')
inventory_fig = px.pie(df, names='Month', values='Inventory Level', title='Inventory Levels')

# Dashboard Layout
app.layout = html.Div(children=[
    html.H1("Mega Mart Data Analytics Dashboard"),
    
    # Sales Performance Line Chart
    html.Div(children=[
        dcc.Graph(
            id='sales-performance',
            figure=sales_fig
        )
    ]),

    # Customer Demographics Bar Chart
    html.Div(children=[
        dcc.Graph(
            id='customer-demographics',
            figure=customers_fig
        )
    ]),

    # Inventory Levels Pie Chart
    html.Div(children=[
        dcc.Graph(
            id='inventory-levels',
            figure=inventory_fig
        )
    ])
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
