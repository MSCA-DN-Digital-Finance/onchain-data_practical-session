
import pandas as pd


def clean_df(result_df):
    result_df['token0Price']  = pd.to_numeric(result_df['token0Price'], errors='coerce')
    result_df['token1Price']  = pd.to_numeric(result_df['token1Price'], errors='coerce')
    result_df['open']  = pd.to_numeric(result_df['open'], errors='coerce')
    result_df['close']  = pd.to_numeric(result_df['close'], errors='coerce')
    result_df['low']  = pd.to_numeric(result_df['low'], errors='coerce')
    result_df['high']  = pd.to_numeric(result_df['high'], errors='coerce')
    result_df['volumeUSD']  = pd.to_numeric(result_df['volumeUSD'], errors='coerce')
    result_df['periodStartUnix'] = pd.to_datetime(result_df['periodStartUnix'], unit='s')
    return result_df