import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    bc_tweets=tweets[tweets['content'].str.len()>15][['tweet_id']]
    return bc_tweets
    