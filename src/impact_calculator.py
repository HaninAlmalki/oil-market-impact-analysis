import pandas as pd
import numpy as np

def calculate_impact_multi(oil_df, date_str, windows=[1,3,7]):
    results = {}

    try:
        dt = pd.to_datetime(date_str)

        if dt not in oil_df.index:
            idx_list = oil_df.index.get_indexer([dt], method='nearest')
            if idx_list[0] == -1:
                return None
            idx = idx_list[0]
        else:
            idx = oil_df.index.get_loc(dt)

        if isinstance(idx, slice):
            idx = idx.start

        for w in windows:
            before = oil_df.iloc[max(0, idx-w):idx]['Close']
            after = oil_df.iloc[idx+1:idx+w+1]['Close']

            if len(before) < w or len(after) < w:
                results[w] = None
                continue

            before_mean = before.mean()
            after_mean = after.mean()

            if before_mean == 0:
                results[w] = 0
            else:
                results[w] = ((after_mean - before_mean) / before_mean) * 100

        return results

    except:
        return None
