import pdb
import pickle
import string
import time
import nltk
import numpy as np
from nltk.corpus import stopwords, twitter_samples
from utils import cosine_similarity, get_dict, process_tweet
from os import getcwd

import w4_unittest

filePath
nltk.data.path.append

en_embeddings_subset
fr_embeddings_subset

en_fr_train
print()
en_fr_test
print()

def get_matrices():
    return X,Y

X_train, Y_train = get_matrices()

w4_unittest.test_get_matrices()

def compute_loss():
    return loss

np.random.seed()
m
n
X
Y
R
print()

w4_unittest.test_compute_loss()

def compute_gradient():
    return gradient

np.random.seed(123)
m = 
n = 
X = 
Y = 
R = 
gradient = 
print()

w4_unittest.test_compute_gradient()


def align_embeddings():
    return R

np.random.seed()
m 
n 
X 
Y 
R 

w4_unittest.test_align_embeddings()
R_train

def nearest_neighbor():
    return k_idx

v = 
candidates
print()

w4_unittest.test_nearest_neighbor()

def test_vocabulary():
    return accuracy

X_val, Y_val = get_matrices()
acc = test_vocabulary()
print()

w4_unittest.unittest_test_vocabulary()

all_positive_tweets
all_negative_tweets
all_tweets

def get_document_embedding():
    return doc_embedding


custom_tweet
tweet_embedding
tweet_embedding

w4_unittest.test_get_document_embedding()

def get_document_vecs():
    return document_vec_matrix, ind2Doc_dict

print()
print()

my_tweet
process_tweet
tweet_embedding

idx
print()

N_VECS
N_DIMS
print()

N_PLANES
N_UNIVERSE

np.random.seed()
planes_l

def hash_value_of_vector():
    return hash_value

np.random.seed(0)
idx
planes
vec
print()

w4_unittest.test_hash_value_of_vector()

def make_hash_table():
    return hash_table, id_table

planes
tmp_hash_table, tmp_id_table 
print()
print()
print()

w4_unittest.test_make_hash_table

def create_hash_tables():
    return hash_tables, id_tables

hash_tables, id_tables = create_hash_id_tables(N_UNIVERSE)

def approximate_knn():
    return nearest_neighbor_ids

doc_id
doc_to_search
vec_to_search

nearest_neighbor_ids

print()
print()
print()

for :
  print()
  print()

w4_unittest.test_approximate_knn()

    
