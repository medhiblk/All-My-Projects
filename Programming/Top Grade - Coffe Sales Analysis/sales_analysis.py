"""
Module for analyzing coffee chain sales.
"""

import pandas as pd
import streamlit as st
import plotly.express as px

# Load the data
CoffeeSales = pd.read_csv('CoffeeSales.csv')

# Ensure the 'Date' column is in datetime format
CoffeeSales['Date'] = pd.to_datetime(CoffeeSales['Date'])
# Sort the data by date to ensure correct plotting
CoffeeSales.sort_values('Date', inplace=True)

# Create a year-month column for grouping
CoffeeSales['YearMonth'] = CoffeeSales['Date'].dt.strftime('%Y-%m')

# Setting page config with a coffee emoji as an icon
st.set_page_config(page_title="Coffee Chain Sales Dashboard", page_icon="☕",
                   initial_sidebar_state="expanded")

# Sidebar for Market Size filter and Analysis Type
with st.sidebar:
    st.title("☕ Coffee Chain Sales Insights")
    st.markdown(
        "This dashboard provides a detailed analysis of coffee product sales, "
        "profits, costs, and margins. It enables users to explore performance "
        "against targets across various market segments over time, offering "
        "valuable insights into business operations and market dynamics."
    )

    # Add a selectbox for the analysis type in the sidebar
    analysis_type = st.selectbox(
        'Select Your Analysis',
        ['Sales', 'Profit', 'Cogs', 'Margin']
    )

    # Add a selectbox for Market Size in the sidebar
    Market_size = CoffeeSales['Market_size'].unique()
    selected_market_size = st.selectbox(
        'Market Size', ['All'] + sorted(Market_size.tolist())
    )

# Apply the selected Market Size filter
if selected_market_size != 'All':
    st.markdown(
        "This dashboard provides a detailed analysis of coffee product sales, "
        "profits, costs, and margins. It enables users to explore performance "
        "against targets across various market segments over time."
    )

# Assuming the column names in the dataset are exactly as follows:
actual_target_mapping = {
    'Sales': 'Target_sales ',
    'Profit': 'Target_profit',
    'Cogs': 'Target_cogs',
    'Margin': 'Target_margin'
}

# Check if the selected analysis type is in the dataframe
CoffeeSales['Type'] = 'Actual'
CoffeeSales_grouped = CoffeeSales.groupby(
    ['YearMonth', 'Type'])[analysis_type].sum().reset_index()

# Merge the actual and target data
target_column = actual_target_mapping.get(analysis_type)
CoffeeSales['Type'] = 'Target'
target_grouped = CoffeeSales.groupby(
    ['YearMonth', 'Type'])[target_column].sum().reset_index()
target_grouped.rename(columns={target_column: analysis_type}, inplace=True)
combined = pd.concat([CoffeeSales_grouped, target_grouped])

# Create and display the combined line chart
with st.container():
    st.header(f'{analysis_type} over Time by Market Size')
    fig = px.line(
        combined,
        x='YearMonth',
        y=analysis_type,
        color='Type',
        title=f'Actual vs Target {analysis_type} Trends',
        labels={'YearMonth': 'Period', analysis_type: analysis_type}
    )
    fig.update_xaxes(title='Period', tickangle=45)
    fig.update_layout(
        legend={
            'title': 'Legend',
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        margin={'l': 20, 'r': 20, 't': 30, 'b': 20}
    )
    st.plotly_chart(fig)
