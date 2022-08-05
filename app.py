import streamlit as st
from helper import market_data
from mainplot import mainplot

# initialize the w2eb page
st.title("Dow Performance by President")
st.subheader("Explore the Dow Jones Industrial performance by President since 1897")

# get the data
data = market_data()

st.pyplot(mainplot(data))