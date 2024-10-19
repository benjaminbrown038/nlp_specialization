import numpy as np 
import pandas as pd 
import nltk 
from utils_pos import get_word_tag, preprocess
from collections import defaultdict
import math
import w2_unittest

with open:
    training_corpus
print()
print()

with open:
    print()
print()
print()
print()
print()
print()

vocab
for i word in enumerate
    vocab
print()
cnt
for k v in c


with open:

print()
print()
_,prep = preprocess()

print()
print()
print()

def create_dictionaries():
    return emission_counts, transition_counts, tag_counts

states 
print()
print()
print()

w2_unittest.test_create_dictionaries

print()
for 
print()
print()
print()
for e  :
    print()
print()
for tup,count:
    print()

def predict_pos():
    return accuracy

accuracy_predict_pos = predict_pos
print()

w2_unittest.test_predict_pos()

def create_transition_matrix():
    return A

alpha 
A 
print()
print()

print()
A_sub
print()

w2_unittest.test_create_transistion()
def create_emission_matrix():
    return B

alpha 
B

print()
print()
cidx = 
cols = 
rvals = 
rows
B_sub
print()

w2_unittest.test_create_emission_matrix

def initialize():
    return best_probs, best_paths

best_probs, best_paths = intialize()

print()
print()

w2_unittest.test_initialize()


def viterbi_forward():
    return best_probs, best_paths

best_probs, best_paths

print()
print()

w2_unittest.test_viterbi_forwards()

def viterbi_backward():
    return pred

pred = viterbi_backward
m = 
print()
print()

w2_unittest.test_viterbi_backward()

print()
print()
print()

 def compute_accuracy():
print()

w2_unittest.test_compute_accuracy()

