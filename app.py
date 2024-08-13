#importing libraries
import streamlit as st
import pandas as pd
import plotly.express as px

#load in the data
cars = pd.read_csv('vehicles_us.csv')

#make a header
st.header ('Car Data Analysis')

#creating a histogram
fig_hist = px.histogram(cars, x='type', color='paint_color',  title='How common colors are on vehicle types')
st.plotly_chart(fig_hist)

#creating a histogram
fig_hist2 = px.histogram(cars, x='model',  color='cylinders',title='Cylinder Type on vehicle brands')
st.plotly_chart(fig_hist2)

#creating a scatterplot
fig_scatter = px.scatter(cars, x='model_year', y='odometer', color='model', title='Odometer of vehicles')
st.plotly_chart(fig_scatter)

#add slider to show display
 # Add a checkbox to show scatter plot
if st.checkbox('Show Scatter Plot'):
    st.plotly_chart(fig_scatter)
filter_cars = st.checkbox('Show only Ford F150')
if filter_cars:
    filtered_cars = cars[cars['model'] == 'ford f150']
else:
    filtered_cars = cars