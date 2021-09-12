import sys
import csv
import json

input_file = sys.argv[1]
output_file = sys.argv[2]

output_fieldnames = [
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
    with open(output_file, 'w', newline = '' ) as o:
        output_writer = csv.DictWriter(o, fieldnames = output_fieldnames, delimiter = ',')
        output_writer.writeheader()
        for line in i:
            row = json.loads(line)
            
            # Tweet is not an original tweet, this data exists
            if 'referenced_tweets' in row.keys():
                
                referenced_tweet_id = row['referenced_tweets'][0]['id']
                reference_type = row['referenced_tweets'][0]['type']
            # Tweet is original tweet
            else:
                referenced_tweet_id = 'None'
                reference_type = 'original_tweet'
            
            output_writer.writerow({
                'lang': row['lang'].replace('\n', ' ').strip(), 
                'conversation_id': row['conversation_id'].replace('\n', ' ').strip(),
                'author_id': row['author_id'].replace('\n', ' ').strip(),
                'created_at': row['created_at'].replace('\n', ' ').strip(),
                'retweet_count': row['public_metrics']['retweet_count'],
                'reply_count': row['public_metrics']['reply_count'],
                'like_count': row['public_metrics']['like_count'],
                'quote_count': row['public_metrics']['quote_count'],
                'text': row['text'].replace('\n', ' ').strip(),
                'referenced_tweet_id': str(referenced_tweet_id),
                'reference_type': str(reference_type),
                'reply_settings': row['reply_settings'].replace('\n', ' ').strip(),
                'id': row['id'].replace('\n', ' ').strip(),
                'author_name': row['author']['name'].replace('\n', ' ').strip(),
                'author_follower_count': row['author']['public_metrics']['followers_count'],
                'author_following_count': row['author']['public_metrics']['following_count'],
                'author_tweet_count': row['author']['public_metrics']['followers_count'],
                'author_listed_count': row['author']['public_metrics']['listed_count'],
                'author_username': row['author']['username'].replace('\n', ' ').strip(),
                'author_verified': row['author']['verified'],
            })


       
                    