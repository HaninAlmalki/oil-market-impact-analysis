import yfinance as yf

def load_oil_data():
    oil = yf.download("BZ=F", start="2015-01-01")
    return oil
