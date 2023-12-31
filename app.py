import pandas as pd
import streamlit as st
import plotly.express as px
import altair

cars = pd.read_csv('vehicles_us.csv')
cars['cylinders'] = cars['cylinders'].fillna(cars.groupby(['model', 'model_year'])['cylinders'].transform('median'))

cond_days_hist = px.histogram(
        cars,
        x="days_listed",
        y="odometer",
        color="condition",
        title='Days Listed Per Condition and Mileage',
        labels={"days_listed": "Days Listed", "odometer": "Mileage", "condition": "Condition"}
    )

cond_days_scatter = px.scatter(
    cars,
    x="days_listed",
    y="odometer",
    color="condition",
    title='Days Listed Per Condition and Mileage',
    labels={"days_listed": "Days Listed", "odometer": "Mileage", "condition": "Condition"}
)

type_price_scatter = px.scatter(
    cars,
    x="type",
    y="price",
    color="condition",
    title='Car Type Prices',
    labels={"type": "Car Type", "price": "Price", "condition": "Condition"}
)

type_price_hist = px.histogram(
    cars,
    x="type",
    y="price",
    color="condition",
    title='Car Type Prices',
    labels={"type": "Car Type", "price": "Price", "condition": "Condition"}
)


st.header('_Listing duration per condition_')

show_histogram = st.checkbox("Histogram")

if show_histogram:
    st.plotly_chart(cond_days_hist, use_container_width=True)
else:
    st.plotly_chart(cond_days_scatter, theme="streamlit", use_container_width=True)


st.header('_Pricing per car type_')

show_scatter = st.checkbox("Revisualize")

if show_scatter:
    st.plotly_chart(type_price_scatter, theme="streamlit", use_container_width=True)
else:
    st.plotly_chart(type_price_hist, use_container_width=True)