from setuptools import setup, find_packages


setup(
    name="streamlit_asset_returns",
    version="0.1.0",

    author="Simon Garisch",
    author_email="gatman946 at gmail.com",

    description="The stylized facts of asset returns using streamlit",
    long_description=open("README.md").read(),

    packages=find_packages(exclude=('tests',)),
    install_requires=[],
)
