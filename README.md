twitter-saxony-anhalt-eletion-2021

## credentials 

search_tweets_v2:
  endpoint: https://api.twitter.com/2/tweets/search/all
  consumer_key: KEY
  consumer_secret: SECRET   

## query

python3 search_tweets.py --credential-file ../../.credentials.yaml --config-file ../../api_config.yaml --output-format a

## links

https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all#tab1

https://stackoverflow.com/questions/27836043/get-tweet-url-having-only-tweet-id/27843083