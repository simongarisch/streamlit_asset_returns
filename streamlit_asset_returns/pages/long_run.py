import streamlit as st
from . data import get_pricing_data


TICKER = "SPY"


def long_run():
    st.title("In the long run the stock market increases.")
    st.markdown("""
        While not necessarily true for individual stocks, the market,
        as measured by an index, tends to go up in the long run.
        There are some basic reasons for this.
        * Investors require a positive expected return for investing in risky assets.
        * Inflation causes the measurement base of stocks ($) to devalue.
    """)

    st.subheader(TICKER)
    df = get_pricing_data(TICKER)
    st.line_chart(df["Adj Close"])
