import nltk
from os import getcwd
import w1_unittest
import numpy as np
import pandas as pd 
from nltk.corpus import twitter_samples
from utils import process_tweet, build_freqs

nltk.download('twitter_samples')
nltk.download('stopwords')

filePath
nltk.data.path.append


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

print()
print()

freqs = 
print()
print()

print()
print()

def sigmoid():
    return h 

if 
else
if
else

w1_unittest.test_sigmoid(sigmoid)

-1 * (1-0) * np.log(1-0.99999)

-1 * np.log(0.00001)

def gradientDescent():

    return J,theta

np.random.seed(1)

tmp_X 
tmp_Y
tmp_J,tmp_theta

print()
print()

w1_unittest.test_gradientDescent(gradientDescent)

def extract_features():
    return x 

tmp1 = extract_features(train_x[0],freqs)
print()

tmp2 = extract_features('blorb bleeeb blooooob',freqs)
print()

w1_unittest.test_extract_features(extract_features,freqs)

X = 
for i in rnage():
    x[] = extract_features()

Y = train_y
J,theta = gradientDescent()
print()
print()

def predict_tweet():
    return y_pred

for tweet in:
  print()

my_tweet
predict_tweet()

w1_unittest.test_predict_tweet()

def test_logistic_regression():
    return accuracy

tmp_accuracy = test_logistic_regression()
print()

w1_unittest.unittest_test_logistic_regression()

print()
for in zip:
    y_hat
    if 
        print()
        print()
        print()

my_tweet
print()
y_hat
print()
if
    print()
else
    print()



  
