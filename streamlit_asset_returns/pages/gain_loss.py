from datetime import datetime
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util


def altair_boxplot(df: pd.DataFrame):
    years = df.Year.values
    min_year, max_year = np.min(years), np.max(years)
    xrange = (min_year, max_year)
    return alt.Chart(df).mark_boxplot().encode(
        x=alt.X("Year", scale=alt.Scale(domain=(xrange))),
        y="Returns",
        tooltip=[
            alt.Tooltip("Year", format=".0f"),
            alt.Tooltip("Returns", format=".4f"),
        ]
    ).properties(
        title="Returns by year",
        width=600,
        height=400,
    )


def gain_loss():
    st.title("Gain / Loss Asymmetry")
    st.markdown("""
        The bull walks up the stairs and the bear jumps out the window.
    """)

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(altair_boxplot))

    df = get_pricing_data(ticker)
    df["Returns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Year"] = [trade_date.year for trade_date in df.index]
    df = df[df["Year"] != 2009]

    desc = df.groupby("Year")["Returns"].describe()
    desc["abs(min) > abs(max)"] = [
        True if abs(minret) > abs(maxret) else False
        for minret, maxret in zip(desc["min"].values, desc["max"].values)
    ]

    first_columns = ["min", "max", "abs(min) > abs(max)"]
    columns = first_columns + [
        col for col in desc.columns if col not in first_columns
    ]
    desc = desc[columns]

    st.subheader(label(ticker))
    st.table(desc)
    st.altair_chart(altair_boxplot(df))
