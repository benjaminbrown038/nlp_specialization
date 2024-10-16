import os 
os.environemnt['TF_CPP_MIN_LOG_LEVEL']

import numpy as np
import pandas as pd 
import tensorflow as tf

import matplotlib.pyplot as plt
import time
import utils 
import textwrap

import w2_unittest

data_dir = "data/corpus"
train_data,test_data = utils.get_train_test_data(data_dir)
example_summary, example_dialogue = train_data.iloc[10]

print()
print()

document, summary = utils.preprocess()
document_test, summary_test = utils.preprocess()

filters = ''
oov_token ''

tokenizer = 
documents_and_summary = pd.concat([])

tokenizer.fit_on_texts()

inputs = 
targets = 

vocab_size 

print()


encoder_maxlen = 
decoder_maxlen = 
inputs = 
targets = 

inputs = 
targets = 

BUFFER = 
BATCH_SIZE = 

dataset = tf.data.Dataset.from_tensor_slices()

def positional_encoding():

    return tf.cast(pos_encoding, dtype = tf.float32)

def create_padding_mask():


def create_look_ahead_mask():

      return mask

def scaled_dot_product_attention():

    return output,attention_weights

q = 
k = 
v = 
mask = 
ou, atw = 
ou = 
atw = 

print()
print()

def FullyConnected():

    return 

class EncoderLayer():

    def __init__():

    def call():

    return encoder_layer_out

class Encoder():
    
    def __init__():

    def call():


class DecoderLayer():

    def __init__():

    def call():


key_dim = 
n_heads = 
decoderLayer_test = 
q = 
encoder_test_output = 
look_ahead_mask =
out, attn_w_b1, attn_w_b2 = 

print()
print()
print()

print()
print()
print()

class Decoder():

    def __init__():

    def call():

n_layers = 5  
emb_d = 13
n_heads = 17
fully_connected_dim = 16
target_vocab_size = 300
maximum_position_encoding = 

x = 
encoder_test_output = 
look_ahead_mask = 
deocder_test = 
outd, att_weights = 

print()
print()
print()

print()
print()
print()
for name,tensor in att_weights.items():
    print()

class Transformer():

    def __init__():

    def call():

        return final_output, attention_weights

n_layers = 
emb_d = 
n_heads = 
fully_connected_dim = 
input_vocab_size = 
target_vocab_size = 
max_positional_encoding_input = 
max_positional_encoding_target = 

transformer = Transformer()

sentence_a = 
sentence_b = 
enc_padding_mask = create_padding_mask()
dec_padding_mask = create_padding_mask()

look_ahead_mask = create_look_ahead_mask()
test_summary, att_weights = transformer()

print()
print()
print()

print()
print()
print()

for name, tensor in att_weights.items():
    print()

num_layers = 2
embedding_dim =  
fully_connected_dim 
num_heads = 
positional_encoding_length = 

transformer = Transformer()

class CustomSchedule():

    def __init__():

    def __call__():


learning_rate = CustomSchedule()
optimizer = tf.keras.optimizers.Adam()

plt.plot()
plt.xlabel()
plt.ylabel()

loss_object = 

def masked_loss():

    return tf.keras.metrics.Mean()


loss = []

@tf.function
def train_step():

    train_loss()

def next_word():

    return predicted_id

input_document = tokenizer.
input_document = 
encoder_input = 

output = 
predicted_token = 
print()

predicted_word = tokenizer
print()

def summarize():

    return tokenizer.

trainin_set_example = 
print()
print()
print()
print()
print()
print()
summarize()

test_example = 
true_summary = summary_test
true_document = document_test

epochs = 

for epochin range():
    
  
