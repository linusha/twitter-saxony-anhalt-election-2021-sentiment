import sys
import csv
from sultan.api import Sultan

s = Sultan()
PATH_TO_API_SCRIPT = ''

input_file = sys.argv[1]
tweets = []
input_fieldnames = [
    'lang', 
    'conversation_id',
    'author_id',
    'created_at',
    'retweet_count',
    'reply_count',
    'like_count',
    'quote_count',
    'text',
    'referenced_tweet_id',
    'reference_type',
    'reply_settings',
    'id',
    'author_name',
    'author_follower_count',
    'author_following_count',
    'author_tweet_count',
    'author_listed_count',
    'author_username',
    'author_verified'
]

with open(input_file, 'r') as i:
    reader = csv.DictReader(i)
    for row in reader:
        tweets.append(row)
    i.close()
print('Read CSV from file.')

original_tweets_authors = [tweet['author_id'] for tweet in tweets if tweet['reference_type'] != 'retweeted' and int(tweet['retweet_count']) > 0]
original_tweets_authors = list(set(original_tweets_authors))
print(len(original_tweets_authors))
restart = original_tweets_authors.index('53723830')
original_tweets_authors = original_tweets_authors[restart:]
print(len(original_tweets_authors))
with Sultan.load(cwd=PATH_TO_API_SCRIPT) as s:
    for user in original_tweets_authors:
        query = f"retweets_of:{user}"
        s.python3(f"search_tweets.py --credential-file ../../.credentials.yaml --config-file ../../api_config.yaml --output-format a --query {query}").run()
