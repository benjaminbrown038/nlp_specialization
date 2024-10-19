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

nltk.download('twitter_samples')
nltk.download('stopwords')

filePath
nlt.data.path.append()

all_positive_tweets = twitter_samples.strings('positive_tweets.json')
all_negative_tweets = twitter_samples.strings('negative_tweets.json')

test_pos
train_pos
test_neg
train_neg

train_x
test_x

train_y
test_y

custom_tweet = 
print()

def count_tweets():
    return result

result 
tweets
ys
count_tweets

w2_unittest.test_count_tweets()
freqs = count_tweets()

def train_naive_bayes():
    return logprior,loglikelihood

logprior,loglikelihood = train_naive_bayes()
print()
print()

w2_unittest.test_train_naive_bayes()

def naive_bayes_predict():
    return p 

my_tweet
p = naive_bayes_predict
print()

w2_unittest.test_naive_bayes_predict()

my_tweet 
p 
print()

def test_naive_bayes():
    return accuracy

print()

for tweet in:
    p 
    print(0)

my_tweet = 
naive_bayes_predict()
w2_unittest.unittest_test_naive_bayes()

def get_ratio():
    return pos_neg_ratio

get_ratio()
w2_unittest.test_get_ratio(get_ratio,freqs)

def get_words_by_threshold():
    return word_list

get_words_by_threshold(freqs,label=0,threshold = 0.5)
get_words_by_threshold(freqs,label=1,threshold = 10)

w2_unittest.test_get_words_by_threshold(get_words_by_threshold,freq)

print()
for x , y in zip():
    y_hat = naive_bayes_predict(x,logprior,loglikehood)
    if y != (np.sign(y_hat)) > 0):
        print()
            process_tweet(x)).encode('ascii','ignore')))

my_tweet 
p 
print()


