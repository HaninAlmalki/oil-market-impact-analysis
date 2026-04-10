import pandas as pd

def summarize_by_type(df):
    return df.groupby("type")["abs_impact"].mean()
