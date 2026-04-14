import yfinance as yf
import pandas as pd

def load_oil_data():
    oil = yf.download("BZ=F", start="2015-01-01")

    if isinstance(oil.columns, pd.MultiIndex):
        oil.columns = oil.columns.get_level_values(0)

    return oil
