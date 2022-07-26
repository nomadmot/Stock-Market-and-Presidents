import streamlit as st
from helper import market_data

# initialize the w2eb page
st.title("Dow Performance by President")
st.subheader("Explore the Dow Jones Industrial performance by President since 1897")

# get the data
df = market_data()
st.dataframe(df)