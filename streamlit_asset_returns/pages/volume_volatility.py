import pandas as pd
import numpy as np
import altair as alt
import streamlit as st
from . data import (
    create_ticker_picker,
    get_pricing_data,
)
from .. import util


def altair_volume_volatility_scatter(df: pd.DataFrame, days: int):
    days_str = str(days) + "Day"
    return_agg = days_str + "AbsReturn"
    volume_agg = days_str + "Volume"
    df[return_agg] = np.abs(df["Returns"].rolling(days).sum())
    df[volume_agg] = df["Volume"].rolling(days).mean()

    return alt.Chart(df).mark_circle(size=60).encode(
        x=volume_agg,
        y=return_agg,
        tooltip=[
            alt.Tooltip(volume_agg, format=",.0f"),
            alt.Tooltip(return_agg, format=".4f"),
        ],
    ).properties(
        title=days_str + " Absolute Return and Volume",
        width=600,
        height=400,
    ).interactive()


def mpl_volume_volatility_line(df: pd.DataFrame, days: int):
    days_str = str(days) + "Day"
    return_agg = days_str + "AbsReturn"
    volume_agg = days_str + "Volume"
    df[return_agg] = np.abs(df["Returns"].rolling(days).sum())
    df[volume_agg] = df["Volume"].rolling(days).mean()
    return df[[volume_agg, return_agg]].plot.line(
        title=days_str + " Absolute Return Vs. Volume",
        subplots=True,
    )


def volume_volatility():
    st.title("Volume Volatility Correlation")
    st.markdown("""
        Trading volume and volatility are positively correlated.
    """)

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()
    days = st.sidebar.slider("Daily returns to aggregate", 1, 252, 1)

    df = get_pricing_data(ticker)
    df["AbsReturn"] = df["Returns"].abs()

    if st.checkbox("Show scatter plot source code"):
        st.markdown(util.python_code_markdown(
            altair_volume_volatility_scatter
        ))
    st.altair_chart(altair_volume_volatility_scatter(df, days))

    if st.checkbox("Show line plot source code"):
        st.markdown(util.python_code_markdown(
            mpl_volume_volatility_line
        ))
    axarr = mpl_volume_volatility_line(df, days)  # noqa: F841
    st.pyplot()
