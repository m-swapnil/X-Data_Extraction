# X (Formerly Twitter) Data Extraction

This repository demonstrates how to extract tweets using the Twitter API v2 and the Tweepy library. The project provides functions to fetch tweets based on keywords or from a specific user's timeline. It also saves the fetched data to CSV files for further analysis.

## Features
- Fetch tweets by keyword.
- Fetch recent tweets from a specific user.
- Save tweets into CSV files for easy analysis.

---

## Prerequisites

Before using the script, ensure you have the following:

1. Python 3.6 or above installed on your machine.
2. Tweepy and Pandas libraries installed:
   ```bash
   pip install tweepy pandas
   ```
3. A Twitter Developer account with API v2 credentials:
   - **Bearer Token**
   - **API Key**
   - **API Secret Key**
   - **Access Token**
   - **Access Token Secret**

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/twitter-data-extraction.git
   cd twitter-data-extraction
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

Update the API credentials in the script:
```python
BEARER_TOKEN = "your_bearer_token"
API_KEY = "your_api_key"
API_SECRET_KEY = "your_api_secret_key"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"
```

---

## Usage

### Fetch Tweets by Keyword
To fetch tweets based on a keyword:
```python
keyword = "BCCI"
keyword_tweets_df = fetch_tweets_by_keyword(keyword)
print(keyword_tweets_df.head())
keyword_tweets_df.to_csv("keyword_tweets.csv", index=False)
```

### Fetch Tweets from a Specific User
To fetch the recent tweets of a specific user:
```python
username = "ICC"
user_tweets_df = fetch_user_tweets(username)
print(user_tweets_df.head())
user_tweets_df.to_csv("user_tweets.csv", index=False)
```

### Run the Script
Execute the script directly to run both examples:
```bash
python twitter_extraction.py
```

---

## Example Output

1. Tweets fetched by keyword are saved in `keyword_tweets.csv`.
2. Tweets fetched from a specific user are saved in `user_tweets.csv`.

---

## File Structure
```
.
|-- twitter_extraction.py      # Main script
|-- requirements.txt           # Required Python packages
|-- keyword_tweets.csv         # Fetched tweets by keyword (generated at runtime)
|-- user_tweets.csv            # Fetched user tweets (generated at runtime)
```

---

## License
This project is licensed under the MIT License.

