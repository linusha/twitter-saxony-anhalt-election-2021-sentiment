twitter-saxony-anhalt-eletion-2021

## credentials 

search_tweets_v2:
  endpoint: https://api.twitter.com/2/tweets/search/all
  consumer_key: KEY
  consumer_secret: SECRET   

## query

python3 search_tweets.py --credential-file ../../.credentials.yaml --config-file ../../api_config.yaml --no-print-stream --output-format a

## links

https://developer.twitter.com/en/docs/twitter-api/tweets/search/api-reference/get-tweets-search-all#tab1

https://stackoverflow.com/questions/27836043/get-tweet-url-having-only-tweet-id/27843083

## Data Collection

Run `transform_json.py` on the `JSON` output of the twitter API to transform it into CSV for further processing. The script takes to arguments on the command line, where the first one is the name of the JSON file to be processed and the second one is the desired name of the output.

## Technical Setup

This code was developed for and used on a UNIX system. If you are on windows, intricacies like line-breaks might need further adjustments in the code.

java -jar SentiStrengthCom.jar input ../tweet_text.csv sentidata ~/twitter-saxony-anhalt-eletion-2021/SentiStrength/SentiStrength_Data/ EmotionLookupTable ~/twitter-saxony-anhalt-eletion-2021/SentiStrength/SentiStrength_Data/EmotionLookupTable_v5_fullforms.txt explain


