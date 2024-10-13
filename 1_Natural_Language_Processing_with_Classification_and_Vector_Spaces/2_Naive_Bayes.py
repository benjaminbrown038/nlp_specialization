from utils import process_tweet, lookup
import pdb 
from nltk.corpus import stopwords, twitter_samples
import numpy as np
import pandas as pd
import nltk
import string
from nltk.tokenize import TweetTokenizer
from os import getcwd
import w2_unittest

nltk.download()
nltk.download()

filePath

all_positive_tweets
all_negative_tweets

test_pos
train_pos
test_neg
train_neg

train_x
test_x

train_y
test_y

custom_tweet = ""
print(process_tweet(custom_tweet))

def count_tweets():

results = 
tweets = 
ys = 
count_tweets()

w2_unittest.test_count_tweets(count_tweets)

freqs = count_tweets()

def train_naive_bayes(freqs,train_x,train_y):

logprior, loglikelihood = train_naive_bayes(freqs,train_x,train_y)
print(logprior)
print(len(loglikelihood))

w2_unittest.test_train_naive_bayes(train_naive_bayes,freqs,train_x,train_y)

def naive_bayes_predict(tweet,logprior,loglikelihood):
    '''
    Input:
        tweet: a string 
        logprior: a number
        loglikelihood: a dictionary of words mapping to numbers
    Output: 
        p: the sum of all the loglikelihoods of each word in the tweet (if found in the dictionary) + logprior (a number) 
    '''



my_tweet = 
p = 
print()

w2_unittest.test_naive_bayes_predict(naive_bayes_predict)

my_tweet = ''
p = naive_bayes_predict()
print('The expected output is: ',p)

def test_naive_bayes():


def get_ratio():


def get_words_by_threshold():



  

