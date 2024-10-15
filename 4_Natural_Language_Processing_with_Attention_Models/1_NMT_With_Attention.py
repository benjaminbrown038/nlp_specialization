import os
os.environ['TF_CPP_MIN_LOG_LEVEL']
import numpy as np
import tensorflow as tf
from collections import Counter
from utils import sentences, train_data, val_data, english_vectorizer, portugese_vectorizer, masked_loss, masked_acc, tokens_to_text
import w1_unittest

portugese_sentences, english_sentences = sentences
print()
print()

del portugese_sentences
del english_sentences
del sentences

print()
print()

vocab_size_por
vocab_size_eng

print()
print()

word_to_id = tf.keras.layers.StringLookup()
id_to_word = tf.keras.layers.StringLookup()

unk_id = word_to_id()
sos_id = word_to_id()
eos_id = word_to_id()
baunilha_id = word_to_id()

print()
print()
print()
print()

for __ in TRAI:


VOCAB_SIZE
UNITS

class Encoder(tf.keras.layers.Layer):
    def __init__():

    def call():


encoder = Encoder(VOCAB_SIZE,UNITS)
encoder_output = encoder(to_translate)

print()
print()

class CrossAttention():
    def __init__():

    def call():

attention_layer = CrossAttention()
sr_translation_embed = tf.keras.layers.Embedding()
attention_result = attention_layer()

print()
print()
print()

class Decoder():
    def __init__():

    def call():

decoder = Decoder()
logits = decoder()

print()
print()
print()

class Translator()
    def __init__():

    def call():

translator - Translator()
logits = translator()

print()
print()
print()

def compile_and_train():


  return model, history

trained_translator, history = compile_and_train(translator)

def generate_next_token(decoder,context,next_token,done,state,temperature):

    return next_token, logit, state, done

eng_sentence = ""
texts = tf.convert_to_tensor()[]
context = english_vectorizer().to_tensor()
context = encoder()

next_token = tf.fill((1,1), sos_id)
state = [tf.random.uniform,tf.random.uniform]
done = False


    





