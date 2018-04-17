import tweepy
import sys
import json


reload(sys)
sys.setdefaultencoding("utf-8")

consumer_key='Aabqg1MkQm2Q5mBTn0it46P16'
consumer_secret='kKokJ72rALiPDzBDFFHXDtHLJHV2fAjMysKLAR7mqqWlwIRzO0'
access_token_key='967815944612532230-MhFNWjmAZr2DLSXcekkJpy0EXNUHeZ1'
access_token_secret='SWavYvxHaaodt1ijGw8aK8WH07ndJKdfW9zzjlXn914a9'


auth=tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

myApi = tweepy.API(auth)

def Query_1():

    tweets = myApi.search(q="amazon OR amzn AND stocks OR stock price OR stock market OR bull OR bear", count=100, lang='en')

    with open('tweets_amzn.txt', 'w') as f:
        for tweet in tweets:
            try:

                f.write('{}\n'.format(tweet.text.decode('utf-8')))
            except BaseException as e:
                print ('ascii codec can\'t encode characters')
            continue



def Query_2():

    tweets = myApi.search(q="intel OR intc AND stock market OR stock price OR stock OR bear OR bull  ", count=100, lang='en')

    with open('tweets_intel.txt', 'w') as f:
        for tweet in tweets:
            try:

                f.write('{}\n'.format(tweet.text.decode('utf-8')))
            except BaseException as e:
                print ('ascii codec can\'t encode characters')
            continue



def Query_3():

    tweets = myApi.search(q="efx ticker OR equifax AND stock market OR stocks OR stock price OR bear OR bull", count=100, lang='en')

    with open('tweets_equifax.txt', 'w') as f:
        for tweet in tweets:
            try:

                f.write('{}\n'.format(tweet.text.decode('utf-8')))
            except BaseException as e:
                print ('ascii codec can\'t encode characters')
            continue



def Query_4():

    tweets = myApi.search(q="dow jones OR nasdaq OR s&p500 AND stock market OR stocks OR bull OR bear", count=100, lang='en')

    with open('tweets_overall_market.txt', 'w') as f:
        for tweet in tweets:
            try:

                f.write('{}\n'.format(tweet.text.decode('utf-8')))
            except BaseException as e:
                print ('ascii codec can\'t encode characters')
            continue


Query_1()
Query_2()
Query_3()
Query_4()