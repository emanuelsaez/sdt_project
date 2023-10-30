import pandas as pd
import streamlit as st
import plotly.express as px
import altair

cars = pd.read_csv('/workspaces/sdt_project/vehicles_us.csv')

st.header('_Listing duration per condition_')

show_histogram = st.checkbox("Revisualize")

if show_histogram:
        cond_days_hist = px.histogram(
        cars,
        x="condition",
        y="days_listed",
    )
    st.plotly_chart(cars_hist, use_container_width=True)
else:
    cond_days_scatter = px.scatter(
        cars,
        x="type",
        y="price",
        color="price"
    )
    st.plotly_chart(cond_days_scatter, theme="streamlit", use_container_width=True)


st.header('_Pricing per car type_')

show_scatter = st.checkbox("Revisualize")

if show_scatter:
    type_price_scatter = px.scatter(
        cars,
        x="type",
        y="price",
        color="price"
    )
    st.plotly_chart(cars_scatter, theme="streamlit", use_container_width=True)
else:
    type_price_hist = px.histogram(
        cars,
        x="type",
        y="price",
    )
    st.plotly_chart(cars_hist, use_container_width=True)