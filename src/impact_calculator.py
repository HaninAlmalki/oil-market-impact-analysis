import pandas as pd
import numpy as np

def calculate_impact(oil_df, date_str, window=3):
    try:
        dt = pd.to_datetime(date_str)
        idx = oil_df.index.get_indexer([dt], method='nearest')[0]

        before = float(oil_df.iloc[idx-window : idx]['Close'].mean())
        after = float(oil_df.iloc[idx+1 : idx+window+1]['Close'].mean())

        if np.isnan(before) or np.isnan(after):
            return None

        return abs(((after - before) / before) * 100)

    except:
        return None
