import math
import streamlit as st
import bokeh.plotting
import numpy as np
from .. import util


def home():
    st.title("Stylized Facts of Asset Returns")
    st.header("What are they?")
    st.write("""
        These are properties of asset returns common to a variety of instruments.
    """)

    st.header("Returns and compounding.")
    st.markdown("""
        Let's first take a look at discrete vs. continuous compounding.

        Suppose we compound a return of 12% over different periods:
        * Compounded annually, 12% compounded once = $(1.12)^{1} - 1 = 12\%$
        * Compounded semi-annually, 12% compounded twice = $(1 + 0.06)^{2} - 1 = 12.36\%$
        * Compounded quarterly, 12% compounded four times = $(1 + 0.03)^{4} - 1 = 12.55\%$
        * Compounded daily, 12% compounded over 365 days = $(1 + 0.12 / 365)^{365} - 1 = 12.747\%$

        If we compound n times then then the result is $$\Big(1 + \\frac{r}{n}\Big)^{n} - 1$$

        Compare this to the formula for $e$ (Euler's number after [Leonhard Euler](https://en.wikipedia.org/wiki/Leonhard_Euler))

        $$e=\lim\limits_{x\\to\infty} \Big(1 + \\frac{1}{n}\Big)^{n}$$

        $e$ is an irrational number = 2.7182818284...
    """)

    st.bokeh_chart(eplot())

    if st.checkbox("Show source code"):
        st.markdown(util.python_code_markdown(eplot))

    st.markdown("""
        If we compound 12% continuously then we get an effective return of $e^{0.12} - 1 = 12.7497\%$ ...

        We can also reverse this to get a continuously compounded (c.c.) rate from our effective rate $=\ln(1 + 12.7497\%) = 12\%$
    """)

    st.header("Proof for continuous compounding.")
    st.markdown("""
    $$(1 + r) = \lim_{n\\to\infty} \Big(1 + \\frac{r_{c}}{n}\Big)^{n}$$

    $$\ln(1 + r) = \lim_{n\\to\infty} n\cdot \ln \Big(1 + \\frac{r_{c}}{n}\Big)$$

    $$\ln(1 + r) = \lim_{n\\to\infty} n\cdot \Big(\\frac{r_{c}}{n}\Big) \ \ \ \ \ [\mathrm{Since} \ \ln(1+x) \\approx x]$$

    $$(1 + r) = \lim_{n\\to\infty} e^{r_{c}} = e^{r_{c}} \ \ \ \ \ \ \ [\mathrm{Taking \ the \ exp}]$$

    $$r = e^{r_{c}} - 1$$
    """)

    st.header("Why are continuously compounded returns useful?")
    st.markdown("""
        We get a stock's return from the price = $\\frac{P_{t}}{P_{t-1}} = (1 + r)$
        and taking $\ln(1 + r)$ gives us the equivalent c.c rate.
        One of the useful properties of c.c. returns is that they are additive,
        so we can use np.cumsum to get the cumulative return over a period. For effective returns:

        $$(1+r_{period}) = (1+r_{1})\cdot (1+r_{2})\cdot (1+r_{3})\cdot \ ... \ \cdot (1+r_{T})$$

        And for c.c returns:

        $$r_{c,period} = \ln\Bigg(\\frac{P_{T}}{P_{0}}\Bigg)$$

        $$= \ln\Bigg(\\frac{P_{1}}{P_{0}} \cdot \\frac{P_{2}}{P_{1}} \cdot \\frac{P_{3}}{P_{2}} \ ... \ \cdot\\frac{P_{T}}{P_{T-1}}\Bigg)$$

        $$= \ln\Bigg(\\frac{P_{1}}{P_{0}}\Bigg) + \ln\Bigg(\\frac{P_{2}}{P_{1}}\Bigg) + \ln\Bigg(\\frac{P_{3}}{P_{2}}\Bigg) + ... + \ln\Bigg(\\frac{P_{T}}{P_{T-1}}\Bigg) = r_{c,1}+r_{c,2}+r_{c,3}+ \ ... \ + r_{c,T}$$
    """)


def eplot():
    """ Plots Euler's number. """
    e = math.exp(1)
    x = np.arange(1, 200)
    y = (1 + 1 / x) ** x

    chart = bokeh.plotting.figure(title="Euler's Number", sizing_mode="stretch_width")
    chart.line(x, y, line_width=2, color="blue")
    chart.line(x, e, line_width=2, color="red")
    chart.xaxis.axis_label = "x"
    chart.yaxis.axis_label = "y"
    return chart
