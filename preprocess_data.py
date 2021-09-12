import sys
import csv
# https://pypi.org/project/DateTime/
from DateTime import DateTime
from statistics import mean
import re

input_file = sys.argv[1]
output_file = sys.argv[2]

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

output_fieldnames = [
    'text',
    'processed_text',
    'lang', 
    'conversation_id',
    'author_id',
    'created_at',
    'retweet_count',
    'reply_count',
    'like_count',
    'quote_count',
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
    'author_verified',
    'retweet_timelag',
    'hashtag_count',
    'url_existence',
    'user_activity'
]

USER_ACTIVITY = {}

#######################################################################
######################## FUNCTION DEFINITIONS #########################
#######################################################################

def remove_urls_from_text(text):
    return re.sub(r'(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]'
                  r'\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|'
                  r'https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.'
                  r'[a-zA-Z0-9]+\.[^\s]{2,})', '', text)

def clean_tweet(tweet):
    # convert to lowercase
    tweet = tweet.lower()
    # remove all email adresses
    tweet = re.sub(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", '', tweet)
    #remove all urls
    tweet = remove_urls_from_text(tweet)
    # remove hashtags but preserve words
    tweet = tweet.replace('#', '')
    return tweet

#######################################################################
############################# MAIN SCRIPT #############################
#######################################################################

tweets = []

with open(input_file, 'r') as i:
    reader = csv.DictReader(i)
    for row in reader:
        tweets.append(row)
    i.close()
print('Read CSV from file.')

original_tweets = [tweet for tweet in tweets if tweet['reference_type'] == 'original_tweet']
# we only need to consider retweets to calculate time lag to first retweet
retweets = [tweet for tweet in tweets if tweet['reference_type'] == 'retweeted']
retweets = [tweet for tweet in tweets if tweet['text'].startswith('RT ')]
print('Split tweets.')

# setup some metrics for evaluation
total = 0
unfound = 0

for original_tweet in original_tweets:
    
    related_tweets = [tweet for tweet in retweets if tweet['text'][tweet['text'].find(': ')+2:] in original_tweet['text']]
    breakpoint()
    if int(original_tweet['retweet_count']) == 0:
        original_tweet['to_delete'] = False
        # by convention -1 is for non-retweeted tweets
        original_tweet['retweet_timelag'] = -1
        total += 1
        continue
    if (len(related_tweets)) == 0 and int(original_tweet['retweet_count']) > 0:
        # entering this branch indicated missing tweets not returned by the twitter API
        unfound += 1
        original_tweet['to_delete'] = True
    if len(related_tweets) == int(original_tweet['retweet_count']) and int(original_tweet['retweet_count']) > 0 :
        # we have all retweets and can guarantee calculating a correct time difference
        time_diffs = [(DateTime(tweet['created_at']) - DateTime(original_tweet['created_at'])) for tweet in related_tweets]
        # convert days to seconds
        original_tweet['retweet_timelag'] = min(time_diffs) * 86400
        original_tweet['to_delete'] = False
    else:
        # entering this branch indicated missing tweets not returned by the twitter API
        print(f"{len(related_tweets)} retweets found but {original_tweet['retweet_count']} should exist for {original_tweet['text']}.")
        unfound += 1
        original_tweet['to_delete'] = True
    total += 1

print(f"{total} tweets in total. {unfound} with problems. They will now be removed.")
print('Calculating retweet-lags completed.')

original_tweets = [original_tweet for original_tweet in original_tweets if original_tweet['to_delete'] == False]
print('Removed original tweets with potential for wrong retweet-lag.')
print(f"{len(original_tweets)} are still being processed.")

for tweet in original_tweets:
        user_for_curr_tweet = tweet['author_id']
        curr_tweet_count_for_user = USER_ACTIVITY.get(user_for_curr_tweet)
        # first tweet we process from that user
        if curr_tweet_count_for_user is None:
            USER_ACTIVITY[user_for_curr_tweet] = 1
        # add one to current tweet count from the user
        else:
            USER_ACTIVITY[user_for_curr_tweet] += 1
print('Finished aggregating user activity for original tweets.')

with open(output_file, 'w') as o:
    output_writer = csv.DictWriter(o, fieldnames=output_fieldnames, delimiter=',')
    output_writer.writeheader()

    for tweet in original_tweets:
        output_writer.writerow({
            'text': tweet['text'],
            'processed_text': clean_tweet(tweet['text']),
            'lang': tweet['lang'], 
            'conversation_id': tweet['conversation_id'],
            'author_id': tweet['author_id'],
            'created_at': tweet['created_at'],
            'retweet_count': tweet['retweet_count'],
            'reply_count': tweet['reply_count'],
            'like_count': tweet['like_count'],
            'quote_count': tweet['quote_count'],
            'referenced_tweet_id': tweet['referenced_tweet_id'],
            'reference_type': tweet['reference_type'],
            'reply_settings': tweet['reply_settings'],
            'id': tweet['id'],
            'author_name': tweet['author_name'],
            'author_follower_count': tweet['author_follower_count'],
            'author_following_count': tweet['author_following_count'],
            'author_tweet_count': tweet['author_tweet_count'],
            'author_listed_count': tweet['author_listed_count'],
            'author_username': tweet['author_username'],
            'author_verified': tweet['author_verified'],
            'retweet_timelag': tweet['retweet_timelag'],
            'hashtag_count': tweet['text'].count('#'),
            'url_existence': '1' if 'http' in tweet['text'] else '0' ,
            'user_activity': USER_ACTIVITY.get(tweet['author_id'])
            })
    o.close()
print('Finished writing output to file.')