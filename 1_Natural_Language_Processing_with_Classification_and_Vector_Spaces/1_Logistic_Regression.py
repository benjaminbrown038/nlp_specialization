import nltk 
from os import getcwd
import w1_unittest
import numpy as np
import pandas as pd
from utils import process_tweet, build_freqs


nltk.download()
nltk.download()

filePath 
nltk.data.path.append(filePath)

all_positive_tweets
all negative_tweets

test_pos
train_pos
test_neg
train_neg

train_x
test_x

train_y
test_y

freqs = build_freqs(train_x,train_y)
print("type(freqs) = " + str(type(freqs)))
print("len(freqs) = " + str(type(freqs.keys())))

def sigmoid():

if (sigmoid(0) == 0.5):
    print('SUCCESS!')
else:  
    print('Oops!')
if (sigmoid(4.92) == 0.9927537604041685):
    print('CORRECT!')
else:
    print('Oops again!')

w1_unttest.test_sigmoid(sigmoid)

-1 * (1-0) * np.log(1-0.9999)
-1 * np.log(0.0001)

def gradientDescent(x,y,theta,alpha,num_iters):
    '''
    Input:
        x:
        y:
        theta:
        alpha:
        num_iters:
    Output:
        J:
        theta:
    Hint:
    '''
    m = None
    for i in range(0,num_iters):
        z = None
        h = None
        J = None 
        theta = None
    J = float(J)
    return J, theta

np.random.seed(1)
tmp_X = np.append(np.ones((10,1)),np.random.rand(10,2) * 2000, 
    


  
