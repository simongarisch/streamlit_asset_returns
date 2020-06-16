import streamlit as st
from . import pages


PAGES = {
    "Home": pages.home,
    "Data Sources": pages.data,
    "Daily Returns Approximately Zero": pages.approx_zero,
    "Peaked with Fat Tails": pages.peaked,
    "Gain / Loss Asymmetry": pages.gain_loss,
    "Volatility Clustering": pages.vol_clustering,
    "Insignificant Autocorrelations": pages.autocorr,
    "Aggregational Gaussianity": pages.agg_gauss,
    "Volume / Volatility Correlation": pages.volume_volatility,
    "The Impact of Tick Sizes": pages.tick_size,
    "Long Run Returns": pages.long_run,
}


def run():
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(PAGES))
    func = PAGES[selection]
    if func is not None:
        func()
