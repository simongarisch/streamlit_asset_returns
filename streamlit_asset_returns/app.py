import streamlit as st
from . import pages


PAGES = {
    "Home": pages.home,
    "Data Sources": pages.data,
    "Daily Returns Approximately Zero": None,
    "Peaked with Fat Tails": None,
    "Gain / Loss asymmetry": None,
    "Volatility Clustering": None,
    "Insignificant Autocorrelations": None,
    "Aggregational Guassianity": None,
    "Volume / Volatility Correlation": None,
    "The Impact of Tick Sizes": None,
}


def run():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES))
    func = PAGES[selection]
    if func is not None:
        func()
