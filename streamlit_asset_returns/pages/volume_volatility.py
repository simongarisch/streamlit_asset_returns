import numpy as np
import altair as alt
import streamlit as st
from bokeh.plotting import figure
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util


def altair_volume_volatility_scatter(df):
    return alt.Chart(df).mark_circle(size=60).encode(
        x="Volume",
        y="AbsReturn",
        tooltip=[
            alt.Tooltip("Volume", format=",.0f"),
            alt.Tooltip("AbsReturn", format=".4f"),
        ],
    ).properties(
        title="Absolute Return and Volume",
        width=600,
        height=400,
    ).interactive()


def volume_volatility():
    st.title("Volume Volatility Correlation")
    st.markdown("""
        Trading volume and volatility are positively correlated.
    """)

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    df = get_pricing_data(ticker)
    df["AbsReturn"] = df["Returns"].abs()

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(
            altair_volume_volatility_scatter
        ))

    st.altair_chart(altair_volume_volatility_scatter(df))
