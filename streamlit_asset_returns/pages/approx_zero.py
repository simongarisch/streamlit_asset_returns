from datetime import datetime
import numpy as np
import streamlit as st
from bokeh.plotting import figure, show
from . data import (
    COMPANIES,
    label,
    get_pricing_data,
)
from .. import util

"""
def make_plot(ticker, returns):
    nona_returns = returns[~np.isnan(returns)]
    hist, edges = np.histogram(nona_returns[1:], density=True, bins=50)
    mu = np.mean(nona_returns)
    sigma = np.std(nona_returns)
    x = np.linspace(-0.05, 0.05, 1000)
    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))

    title = ticker + "Returns Distribution (μ=%0.2f%%, σ=%0.2f%%)"
        % (round(mu * 100, 2), round(sigma * 100, 2))

    p = figure(title=title, tools="", background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend_label="PDF")
    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = "x"
    p.yaxis.axis_label = "Pr(x)"
    p.grid.grid_line_color="white"
    return p
"""

def approx_zero():
    st.title("Daily Returns Approximately Zero")
    st.markdown("""
        The daily mean return is very close to zero for most stocks.
    """)

    st.sidebar.subheader("Ticker")
    ticker = st.sidebar.selectbox(
        "Select a ticker",
        COMPANIES.index.sort_values(),
        index=3,
        format_func=label,
    )

    start = datetime(2010, 1, 1).date()
    end = datetime.now().date()
    df = get_pricing_data(ticker, start, end).copy()
    returns = np.log(df["Adj Close"] / df["Adj Close"].shift(1))
    df["Returns"] = returns
