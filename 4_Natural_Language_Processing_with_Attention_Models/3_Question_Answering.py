import os 

import traceback
import time
import json
from termcolor import colored
import string

import textwrap
import itertools
import numpy as np
import tensorflow_text as tf_text

import tensorflow as tf
import transformer_utils
import utils

import w3_inittest


data_dir = "data/corpus"
train_data, test_data = utils.get_train_test_data(data_dir)
example_summary, example_dialogue = train_data.iloc[10]

print()
print()

document, summary = utils.preprocess()
document_test, summary_test = utils.preprocess()

filters = ''
oov_token = ''

tokenizer = tf.keras.preprocessing.text.Tokenizer()
documents_and_summary = pf.concat([])

tokenizer.fit_on_texts(documents_and_summary)

inputs = tokenizer.texts_to_sequences(document)
targets = tokenizer.texts_to_sequences(summary)

vocab_size = len()

print()

encoder_maxlen = 
decoder_maxlen = 

inputs 
targets

inputs 
targets

BUFFER_SIZE
BATCH_SIZE

dataset

def positional_encoding():

    return tf.cast(pos_encoding, dtype=tf.float32)

def create_padding_mask(decoder_token_ids):

    return 

def create_look_ahead_mask():

    return mask

def scaled_dot_product_attentions():

    return output, attention_weights


q = 
k = 
v = 
mask = 
ou,atw = 
ou = 
atw = 

print()
print()

def FullyConnected(embedding_dim,fully_connected_dim):
    return 

class EncoderLayer():

    def __init__():

    def call():

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
out, attn_w_b1, attn_w_b2 = decoderLayer_test()

print()
print()
print()

print()
print()
print()

class Decoder():

    def __init__():

    def call():



n_layers = 
emb_d = 
n_heads = 
fully_connected_dim = 
target_vocab_size = 
maximum_position_encoding = 

x = 
encoder_test_output = tf.conver_to_tensor()
look_ahead_mask = create_look_ahead_mask()
decoder_test = Decoder()
outd, att_weights = decoder_test()

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
sentence_b 

enc_padding_mask = 
dec_padding_mask = 

look_ahead_mask = 
test_summary, att_weights = transformer()

print()
print()
print()

print()
print()
print()
for name, tensor in att_weights.items():
    print()


num_layers = 
embedding_dim 
fully_connected_dim 
num_heads = 
positional_encoding_length
transformer = 

class CustomSchedule():

    def __init__():

    def __call__():


learning_rate = CustomSchedule()
optimizer = tf.keras.optimizer.Adam()

plt.plot()
plt.ylabel()
plt.xlabel()
loss_object = tf.keras

def masked_loss():

    return tf.reduce_sum(loss_)/tf.reduce_sum(mask)

train_loss = tf.keras.metrics.Mean(name = 'train_loss')
losses = []

@tf.function
def train_step():
    train_loss(loss)

def next_word(model,encoder_input,output):
    return predicted_id

input_document = tokenizer.
input_document = tf.keras.preprocessing.sequence.pad_sequences()
encoder_input = tf.expand_dims()
output = tf.expand_dims()

predicted_token = next_word()
predicted_word = tokenizer.sequences_to_texts()

def summarize():
    return tokenizer.sequences_to_texts()

training_set_example = 0 
print()
print()
print()
print()
print()
summarize()

test_example = 
true_summary = summary_test[]
true_document = document_test[]

epochs = 

for epoch in range():
    start = 
    train_loss.reset_states()
    number_of_batches = 
    for (batch,(inp,tar) in enumerate(dataset))_
