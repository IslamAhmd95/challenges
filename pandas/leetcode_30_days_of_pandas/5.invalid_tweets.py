#  Problem: Invalid Tweets
#  Link: https://leetcode.com/problems/invalid-tweets/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets[tweets['content'].str.len() > 15][['tweet_id']]

tweets = {
    'tweet_id': [1, 2],
    'content': ['Let us Code', 'More than fifteen chars are here!']
}

tweets_df = pd.DataFrame(tweets)
print(invalid_tweets(tweets_df))