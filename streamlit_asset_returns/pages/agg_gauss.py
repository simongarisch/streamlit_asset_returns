import pandas as pd
import numpy as np
import streamlit as st
from bokeh.plotting import figure
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util


def create_agg_dist_plot(
    ticker: str,
    df: pd.DataFrame,
    days: int,
):
    df["AggReturns"] = np.log(df["Adj Close"] / df["Adj Close"].shift(days))
    returns = df["AggReturns"].values
    nona_returns = returns[~np.isnan(returns)]
    hist, edges = np.histogram(nona_returns, density=True, bins=50)
    mu = np.mean(nona_returns)
    sigma = np.std(nona_returns)
    min_ret, max_ret = np.min(nona_returns), np.max(nona_returns)
    x = np.linspace(min_ret, max_ret, 1000)
    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

    title = ticker + " %d Day Returns Distribution (μ=%0.2f%%, σ=%0.2f%%)" % (days, round(mu * 100, 2), round(sigma * 100, 2))

    p = figure(title=title, tools="", background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend_label="PDF")
    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = "Return"
    p.yaxis.axis_label = "Pr(Return)"
    p.grid.grid_line_color="white"
    return p


def agg_gauss():
    st.title("Aggregational Gaussianity")
    st.markdown("""
        As we aggregate our daily returns they move towards a normal distribution.
    """)

    st.sidebar.subheader("Ticker")
    ticker = create_ticker_picker()

    days = st.sidebar.slider("Daily returns to aggregate", 1, 252, 1)

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(create_agg_dist_plot))

    df = get_pricing_data(ticker)
    st.bokeh_chart(create_agg_dist_plot(ticker, df, days))
