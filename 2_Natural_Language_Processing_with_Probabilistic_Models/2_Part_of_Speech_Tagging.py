from utils_pos import get_word_tag, preprocess
import pandas as pd 
from collections import defaultdict
import math
import numpy as np
import w2_unittest

def create_dictionaries():

    return emission_counts, transition_counts, tag_counts


def predict_pos():

    return accuracy


def create_transition_matrix():

    return A


def create_emission_matrix():

    return B


def initialize():

    return best_probs, best_paths


def viterbi_forward():

    return best_probs, best_paths


def viterbi_backward():

    return pred


def compute_accuracy():

    return num_correct/total

