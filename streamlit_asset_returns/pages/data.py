from datetime import datetime
import pandas as pd
import pandas_datareader.data as web
import streamlit as st
from .. import util


URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"


@st.cache
def collect_sp500_companies() -> pd.DataFrame:
    """ Returns a pandas dataframe containing all stocks in the S&P 500. """
    df_list = pd.read_html(URL)
    return df_list[0].fillna(0).set_index("Symbol").drop("SEC filings", axis=1)


COMPANIES = collect_sp500_companies()


def label(symbol):
    row = COMPANIES.loc[symbol]
    return symbol + " - " + row.Security


@st.cache
def get_pricing_data(
    ticker: str,
    start: datetime.date,
    end: datetime.date
) -> pd.DataFrame:
    """ Returns a pandas dataframe of prices. """
    return web.DataReader(ticker, "yahoo", start, end)


def data():
    st.title("Data Sources")

    st.sidebar.subheader("S&P 500 Stocks")
    st.subheader("S&P 500 Stocks")
    st.markdown("""
        We've collected all stocks in the S&P 500 from
        [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies) 
    """)

    if st.checkbox("S&P 500 Stocks - Show source code"):
        st.markdown(util.python_code_markdown(collect_sp500_companies))

    if st.sidebar.checkbox("View Wikipedia company list", False):
        st.table(COMPANIES)

    st.subheader("Pricing Data")
    st.markdown("""
        Pricing is collected from yahoo finance using
        [pandas_datareader](https://github.com/pydata/pandas-datareader) 
    """)
    if st.checkbox("Pricing Data - Show source code"):
        st.markdown(util.python_code_markdown(get_pricing_data))

    st.sidebar.subheader("Pricing Data")
    ticker = st.sidebar.selectbox(
        "Select a ticker",
        COMPANIES.index.sort_values(),
        index=3,
        format_func=label,
    )

    start = datetime(2010, 1, 1).date()
    end = datetime.now().date()
    df = get_pricing_data(ticker, start, end).copy()
    st.line_chart(df["Adj Close"])
