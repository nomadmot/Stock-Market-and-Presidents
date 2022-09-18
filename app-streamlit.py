import streamlit as st
import plot_presidents as pp

# initialize the web page
st.title("Dow Performance by President")
st.subheader("Explore the Dow Jones Industrial performance by President since 1897")


# add selection checkboxes
st.checkbox("Show Presidents", value=True, key="presidents")
st.checkbox("Show Market", value=True, key="market")

# create the chart
st.plotly_chart(
    pp.create_chart(
        st.session_state.presidents,
        st.session_state.market
    )
)