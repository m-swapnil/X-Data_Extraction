# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 22:14:48 2025

@author: Swapnil Mishra
"""

# Install Tweepy if not already installed
# pip install tweepy pandas

import tweepy
import pandas as pd

# Twitter API v2 credentials
BEARER_TOKEN = "give_your_bearer_token"  # Replace with your Bearer Token
API_KEY = "your_api_key"            # Replace with your API Key
API_SECRET_KEY = "Give_yours"  # Replace with your API Secret Key
ACCESS_TOKEN = "give_yours"  # Replace with your Access Token
ACCESS_TOKEN_SECRET = "give_yours"  # Replace with your Access Token Secret

# Initialize the client
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
)

# Function to search tweets by keyword
def fetch_tweets_by_keyword(keyword, max_results=100):
    """
    Fetch tweets by a specific keyword.
    :param keyword: The keyword to search for.
    :param max_results: The number of tweets to fetch (max is 100 per request).
    :return: A DataFrame containing the fetched tweets.
    """
    response = client.search_recent_tweets(
        query=keyword, 
        max_results=max_results, 
        tweet_fields=['text', 'author_id', 'created_at']
    )
    tweets = [{'AuthorID': tweet.author_id, 'Text': tweet.text, 'CreatedAt': tweet.created_at} for tweet in response.data]
    return pd.DataFrame(tweets)

# Function to fetch a user's tweets
def fetch_user_tweets(username, max_results=100):
    """
    Fetch the recent tweets from a specific user.
    :param username: The username of the target account.
    :param max_results: The number of tweets to fetch (max is 100 per request).
    :return: A DataFrame containing the user's tweets.
    """
    # Get user ID from username
    user = client.get_user(username=username)
    user_id = user.data.id

    response = client.get_users_tweets(
        id=user_id,
        max_results=max_results,
        tweet_fields=['text', 'created_at']
    )
    tweets = [{'Text': tweet.text, 'CreatedAt': tweet.created_at} for tweet in response.data]
    return pd.DataFrame(tweets)

# Example Usage
if __name__ == "__main__":
    # Fetch tweets by keyword
    keyword = "BCCI"
    keyword_tweets_df = fetch_tweets_by_keyword(keyword)
    print("Tweets fetched by keyword:")
    print(keyword_tweets_df.head())
    keyword_tweets_df.to_csv("keyword_tweets.csv", index=False)

    # Fetch tweets from a specific user
    username = "ICC"
    user_tweets_df = fetch_user_tweets(username)
    print(f"\nTweets from {username}:")
    print(user_tweets_df.head())
    user_tweets_df.to_csv("user_tweets.csv", index=False)

    print("\nTweet extraction complete. Data saved to CSV files.")