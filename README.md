# Sentiment Analysis on Tweets

## Notes
---
- Downloading Anaconda / Conda for Step 3 and 4 below are optional.
- We will be using Python 3.
- Authenticate with Twitter *before* moving onto installation if you have not.

## Authenticating with Twitter
---
1. Go to [apps.twitter.com](https://apps.twitter.com/)
2. You want to `Create New App`
3. Type in the `name`, `description`, and `website` of your app. Any info, or string, is fine.
4. Agree to the `Twitter Agreement` and `Create your Twitter application`
5. Collect your `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret`. Add them into the `/twitter_sentiment/secrets.py`.

## Installation
---
1. Clone the repo: `$ git clone `
2. Change into directory: `$ cd twitter_sentiment`
3. Create the environment: `$ conda create -n twitter_sentiment python=3`
4. Activate it: `$ source activate twitter_sentiment`
5. Install requirements `$ pip install -r requirements.txt`
6. `$ python3 generate_csv.py <YOUR TOPIC>`
