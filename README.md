# Twitter-Topic-Sentiment-Bot
A program that checks twitter sentiment on different topics. This twitter bot uses the Tweepy python library to access the Twitter API. It also uses the pretrained SentimentIntensityAnalyzer from the python NLTK library to find the sentiment of the tweets returned from the Twitter API and returns the average sentiment of a tweet search on a topic inputed by the user.

# Requirments
Before using the program, ensure you have python3 is downloaded as well as the Tweepy and NLTK python libraries. You need to have a twitter developer account with a elevated access to the twitter API. 

# Usage
Create a project using the twitter API and collect the consumer key, consumer secret, access token and access token secret.
After installing python3 and the required modules (see Requirments above). Open the terminal. Now perform a git clone: 
``` 
git clone https://github.com/bdakhel/Twitter-Topic-Sentiment-Bot.git
```
Type into the terminal:
```
cd Twitter-Topic-Sentiment-Bot
```
Open the python file using vim:
```
vim twitter-sentiment-bot.py
```
Replace:
(consumer_key, consumer_secret,
    access_token, access_token_secret)
With the strings of your consumer key, consumer secret, access token and access token secret (each between quotes).
Type ```:wq``` to return to the terminal.
Type into the terminal: 
```
python3 twitter-sentiment-bot.py
```
Now type your topic to check sentiment for. Sentiment should be printed in the terminal.


