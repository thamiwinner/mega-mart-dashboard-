import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data
sales_data = {
    'Month': ['January', 'February', 'March', 'April', 'May', 'June'],
    'Total Sales': [50000, 52000, 55000, 60000, 58000, 62000],
}
customer_data = {
    'Age Group': ['18-25', '26-35', '36-45', '46-60', '60+'],
    'Buying Trends': [70, 65, 60, 55, 50],
}
inventory_data = {
    'Product': ['A', 'B', 'C', 'D', 'E'],
    'Stock': [100, 50, 75, 20, 10],
}
marketing_data = {
    'Campaign': ['Campaign 1', 'Campaign 2', 'Campaign 3', 'Campaign 4'],
    'ROI (%)': [15, 12, 18, 10],
}

df_sales = pd.DataFrame(sales_data)
df_inventory = pd.DataFrame(inventory_data)
df_marketing = pd.DataFrame(marketing_data)

# Create visualizations
sales_fig = px.line(df_sales, x='Month', y='Total Sales', title='Sales Performance Over Time')
inventory_fig = px.bar(df_inventory, x='Product', y='Stock', title='Current Inventory Levels')
marketing_fig = px.bar(df_marketing, x='Campaign', y='ROI (%)', title='Marketing ROI')

# App Layout
app.layout = html.Div([
    # Header with title, motto, and search input
    html.Div([
        html.Div([
            #html.Img(src='https://via.placeholder.com/40', style={'height': '40px', 'margin-right': '10px'}),
            html.H1("Retail Insights Hub", style={'color': '#fff', 'margin': '0', 'font-size': '24px'}),
        ], style={'display': 'flex', 'align-items': 'center'}),
        html.Div([
            html.P("Your source for actionable business insights", style={'color': '#ddd', 'margin': '0', 'font-size': '14px', 'text-align': 'center'}),
        ], style={'flex': '1', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        html.Div([
            dcc.Input(id="search-input", type="text", placeholder="Search...", style={'padding': '8px', 'width': '150px', 'border-radius': '20px', 'border': '1px solid #444'}),
            html.Button(html.I(className='fas fa-search'), id='search-button', n_clicks=0, style={'padding': '8px', 'font-size': '16px', 'border': 'none', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '20px', 'margin-left': '5px', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
        ], style={'float': 'right', 'display': 'flex', 'align-items': 'center'}),
    ], style={'backgroundColor': '#1F2C42', 'padding': '10px', 'color': '#fff', 'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}),

    # Left menu and main content
    html.Div([
        # Left Menu: Reduced size, dark-colored buttons with advanced corners
        html.Div([
            html.Button('📊 Sales Performance', id='btn-sales', n_clicks=0, 
                        style={'font-size': '14px', 'padding': '10px', 'width': '100%', 'margin-bottom': '12px', 'height': '50px', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '15px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
            html.Button('👥 Customer Demographics', id='btn-customer', n_clicks=0, 
                        style={'font-size': '14px', 'padding': '10px', 'width': '100%', 'margin-bottom': '12px', 'height': '50px', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '15px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
            html.Button('📦 Inventory Levels', id='btn-inventory', n_clicks=0, 
                        style={'font-size': '14px', 'padding': '10px', 'width': '100%', 'margin-bottom': '12px', 'height': '50px', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '15px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
            html.Button('📈 Marketing Effectiveness', id='btn-marketing', n_clicks=0, 
                        style={'font-size': '14px', 'padding': '10px', 'width': '100%', 'margin-bottom': '12px', 'height': '50px', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '15px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
            html.Button('🚚 Supply Chain Efficiency', id='btn-supply-chain', n_clicks=0, 
                        style={'font-size': '14px', 'padding': '10px', 'width': '100%', 'margin-bottom': '12px', 'height': '50px', 'backgroundColor': '#2E3B4E', 'color': '#fff', 'border-radius': '15px', 'box-shadow': '0px 4px 6px rgba(0, 0, 0, 0.1)'}),
        ], style={'width': '16%', 'backgroundColor': '#1F2C42', 'padding': '8px', 'color': '#fff', 'height': '100vh', 'position': 'sticky', 'top': '0', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'flex-start', 'padding-top': '20px', 'padding-bottom': '20px'}),

        # Main content area for metric displays
        html.Div(id='content-area', children=[
            dcc.Graph(id='main-chart', figure=sales_fig, style={'height': '88vh'})
        ], style={'width': '84%', 'padding': '8px', 'backgroundColor': '#1C1C1C', 'height': '100vh', 'overflow': 'auto'})
    ], style={'display': 'flex', 'height': '100vh', 'overflow': 'hidden'}),
])

# Callback to update the displayed chart based on button clicks
@app.callback(
    Output('main-chart', 'figure'),
    [Input('btn-sales', 'n_clicks'),
     Input('btn-customer', 'n_clicks'),
     Input('btn-inventory', 'n_clicks'),
     Input('btn-marketing', 'n_clicks'),
     Input('btn-supply-chain', 'n_clicks')]
)
def update_content(btn_sales, btn_customer, btn_inventory, btn_marketing, btn_supply_chain):
    ctx = dash.callback_context
    if not ctx.triggered:
        return sales_fig
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if button_id == 'btn-sales':
        return sales_fig
    elif button_id == 'btn-customer':
        return px.pie(names=customer_data['Age Group'], values=customer_data['Buying Trends'], title="Customer Demographics")
    elif button_id == 'btn-inventory':
        return inventory_fig
    elif button_id == 'btn-marketing':
        return marketing_fig
    elif button_id == 'btn-supply-chain':
        return px.line(x=['January', 'February', 'March'], y=[95, 97, 96], title="Supply Chain Efficiency")
    return sales_fig  # Default figure if no button is clicked

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
