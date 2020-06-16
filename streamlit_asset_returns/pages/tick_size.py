import streamlit as st
from .data import get_pricing_data
from .. import util


TICKER = "COE.AX"


def mpl_chart_hist():
    df = get_pricing_data(TICKER).dropna()
    return df["Returns"].plot.hist(
        title=TICKER + " Returns Histogram",
        bins=100,
    )


def tick_size():
    st.title("The Impact of Tick Sizes")
    st.subheader(TICKER)

    st.markdown("""
        Minimum price steps are discrete and
        [defined by the exchange](https://www.asx.com.au/services/trading-services/price.htm).
        Many models of returns assume that they are drawn from a continuous distribution,
        but price steps mean that only specific return values are possible for a given price.
        Here we use Cooper Energy (COE.AX) as an example as the minimum tick size of 1/2 cent
        is meaningful for a stock price of $0.385 (at the time of writing).

        $0.005/0.385 = 1.3\%$

        Given the current price, returns between 0 - 1.3% are not possible.

        Gaps start to appear when charting a histogram of returns...
    """)

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(mpl_chart_hist))
    plot = mpl_chart_hist()  # noqa: F841
    st.pyplot()
