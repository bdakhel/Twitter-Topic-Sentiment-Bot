import tweepy
import re
from nltk.sentiment import SentimentIntensityAnalyzer

# Search for english tweets, excluding retweets
def search(query,max_results):
    
    # Login
    client = tweepy.Client(consumer_key, consumer_secret,
    access_token, access_token_secret)
    
    # Search recent tweets with query
    response = client.search_recent_tweets(query,max_results=max_results)
    data = response.data 

    return data

# Remove links, authors name and @'s
def clean_data(tweet_search):
    
    # Initialize list of tweets
    tweet_list = []
    
    for tweet in tweet_search:
        
        # Remove links
        linkless = re.sub(r'http\S+','',tweet.text)
       
        # Remove @'s
        atless = re.sub(r'@','',linkless)
        
        # Add to list of tweets
        tweet_list.append(atless)
    return tweet_list

# Analyze list of strings and return sentiments with string
def get_sentiments(tweet_list):
    
    # Create an instance of SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()
    
    # Initialize dictionary of tweets and sentiments
    tweet_sent = dict()
    
    for tweet in tweet_list:
        
        # Get each sentiment
        sentiment = sia.polarity_scores(tweet)
        
        # Pair each tweet with its sentiment
        tweet_sent[tweet] = sentiment

    return tweet_sent

# Attain a summary of results
def summary_results(tweet_sent):
    
    # Attain total number of tweets after cleaning
    total = len(tweet_sent)

    # Initialize sums
    neu_sum, neg_sum, pos_sum, com_sum = 0, 0, 0, 0
    
    # Count each sum
    for k in tweet_sent:
        neu_sum += tweet_sent[k]['neu']
        neg_sum += tweet_sent[k]['neg']
        pos_sum += tweet_sent[k]['pos']
        com_sum += tweet_sent[k]['compound']
    
    # Compute each average 
    neu_avg = neu_sum/total
    neg_avg = neg_sum/total
    pos_avg = pos_sum/total
    com_avg = com_sum/total
    print(f'Neutral average is {neu_avg:.2f}, Negative average is {neg_avg:.2f}, Positive average is {pos_avg:.2f}, Compound average is {com_avg:.2f}, Total number of tweets checked are {total}')
    return

query = input('Enter the topic you\'d like to check twitter sentiment for: ')
tweet_search = search(query,100)
tweet_list = clean_data(tweet_search)
tweet_sent = get_sentiments(tweet_list)
summary_results(tweet_sent)
