import altair as alt
import streamlit as st
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util


def altair_abs_returns_scatter(df):
    return alt.Chart(df).mark_circle(size=60).encode(
        x="AbsReturnLag",
        y="AbsReturn",
        tooltip=[
            alt.Tooltip("AbsReturnLag", format=".4f"),
            alt.Tooltip("AbsReturn", format=".4f"),
        ],
    ).properties(
        title="Return vs Lagged Return",
        width=600,
        height=400,
    ).interactive()


def altair_abs_returns_plot(df):
    df["Date"] = df.index.values
    return alt.Chart(df).mark_circle(size=60).encode(
        x="Date",
        y="AbsReturn",
        color=alt.Color(
            "AbsReturn",
            scale=alt.Scale(scheme="blues")
        ),
        tooltip=[
            alt.Tooltip("Date", format="%Y/%m/%d"),
            alt.Tooltip("AbsReturn", format=".4f"),
        ],
    ).properties(
        title="Absolute Daily Returns",
        width=600,
        height=400,
    )


def vol_clustering():
    st.title("Volatility Clustering")

    st.write("""
        Abnormally sized returns tend to cluster.
        Here we use absolute returns as a measure of volatility.
    """)
    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    df = get_pricing_data(ticker)
    df["AbsReturn"] = df["Returns"].abs()
    df["AbsReturnLag"] = df["AbsReturn"].shift(1)

    st.subheader(label(ticker))
    if st.checkbox("Show scatter plot source code"):
        st.markdown(util.python_code_markdown(
            altair_abs_returns_scatter
        ))
    st.altair_chart(altair_abs_returns_scatter(df))

    if st.checkbox("Show line plot source code"):
        st.markdown(util.python_code_markdown(
            altair_abs_returns_plot
        ))
    st.altair_chart(altair_abs_returns_plot(df))
