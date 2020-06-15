import streamlit as st


def vol_clustering():
    st.title("Volatility Clustering")

    st.write("""
        Abnormally sized returns tend to cluster.
        Here we use absolute returns as a measure of volatility.
    """)