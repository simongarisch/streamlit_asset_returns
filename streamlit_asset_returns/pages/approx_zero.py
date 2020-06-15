from datetime import datetime
import numpy as np
import streamlit as st
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)


def approx_zero():
    st.title("Daily Returns Approximately Zero")
    st.markdown("""
        The daily mean return is very close to zero for most stocks.
    """)

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    df = get_pricing_data(ticker)
    returns = np.log(df["Adj Close"] / df["Adj Close"].shift(1))

    st.subheader(label(ticker))
    st.table(returns.describe())
