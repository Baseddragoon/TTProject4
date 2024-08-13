import streamlit as st
import pandas as pd
import plotly.express as px

# Load the data
cars = pd.read_csv('vehicles_us.csv')

# Display header
st.header('Car Data Analysis')

# Add a checkbox to filter data
filter_cars = st.checkbox('Show only SUVs')

if filter_cars:
    # Filter the DataFrame to show only SUVs
    filtered_cars = cars[cars['type'] == 'SUV']
else:
    # Show the original DataFrame if checkbox is not checked
    filtered_cars = cars

# Creating a histogram
fig_hist = px.histogram(filtered_cars, x='type', color='paint_color', title='How common colors are on vehicle types')
st.plotly_chart(fig_hist)

# Creating a second histogram
fig_hist2 = px.histogram(filtered_cars, x='model', color='cylinders', title='Cylinder Type on vehicle brands')
st.plotly_chart(fig_hist2)

# Creating a scatterplot
fig_scatter = px.scatter(filtered_cars, x='model_year', y='odometer', color='model', title='Odometer of vehicles')
st.plotly_chart(fig_scatter)

# Add a checkbox to show scatter plot
if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(fig_scatter)