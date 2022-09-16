import streamlit as st
import plot_presidents as pp

# initialize the w2eb page
st.title("Dow Performance by President")
st.subheader("Explore the Dow Jones Industrial performance by President since 1897")

# create the basic chart
fig = pp.create_figure()
pp.add_chart_presidents(fig)
pp.add_chart_market(fig)

st.plotly_chart(fig)