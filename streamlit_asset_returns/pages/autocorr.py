import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
import streamlit as st
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util
plt.style.use("seaborn")


def mpl_plot_acf(df):
    """ Plot returns autocorrelation using matplotlib. """
    fig, ax = plt.subplots(1)

    returns = df["Returns"].values
    nona_returns = returns[~np.isnan(returns)]

    plot_acf(
        nona_returns,
        ax=ax,
        lags=20,
        alpha=0.05,
        use_vlines=True,
        unbiased=False,
        fft=False,
        title="Daily Returns Autocorrelation",
        zero=False,
    )
    return fig


def autocorr():
    st.title("Insignificant Autocorrelations")
    st.markdown("""
        The correlation of time series observations with observations from previous time steps,
        called lags, is known as the autocorrelation / lagged correlation / serial correlation.
        The lack of autocorrelation suggests that a stock's return on previous days in itself
        gives us little information about today's return.
    """)

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(mpl_plot_acf))

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    st.subheader(label(ticker))
    df = get_pricing_data(ticker)
    fig = mpl_plot_acf(df)  # noqa: F841
    st.pyplot()
