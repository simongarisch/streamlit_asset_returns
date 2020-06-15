import numpy as np
import streamlit as st
from bokeh.plotting import figure
from . data import (
    create_ticker_picker,
    label,
    get_pricing_data,
)
from .. import util


def volume_volatility():
    st.title("Volume Volatility Correlation")
    st.markdown("""
        Trading volume and volatility are positively correlated.
    """)
