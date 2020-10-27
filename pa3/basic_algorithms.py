"""
CS121: Analyzing Election Tweets (Solutions)

Algorithms for efficiently counting and sorting distinct `entities`,
or unique values, are widely used in data analysis.

Functions to implement:

- count_tokens
- find_top_k
- find_min_count
- find_most_salient

You may add helper functions.
"""

import math
from util import sort_count_pairs

def count_tokens(tokens):
    '''
    Counts each distinct token (entity) in a list of tokens

    Inputs:
        tokens: list of tokens (must be immutable)

    Returns: dictionary that maps tokens to counts
    '''
    dic_count_tokens = {}
    for token in tokens: 
        if token not in dic_count_tokens:
            dic_count_tokens[token] = 1
        else:
            dic_count_tokens[token] += 1
    
    return dic_count_tokens



def find_top_k(tokens, k):
    '''
    Find the k most frequently occuring tokens

    Inputs:
        tokens: list of tokens (must be immutable)
        k: a non-negative integer

    Returns: list of the top k tokens ordered by count.
    '''

    #Error checking (DO NOT MODIFY)
    if k < 0:
        raise ValueError("In find_top_k, k must be a non-negative integer")

    # YOUR CODE HERE
    frequency = count_tokens(tokens)
    lst_frequency = []
    lst_descend = []

    for entry in frequency.items():
        lst_frequency.append(entry)
    lst_descend = sort_count_pairs(lst_frequency)
    
    top_k = []
    if k <= len(lst_descend):
        for i in range(k):
            top_k.append(lst_descend[i][0])
    else:
        for i in range(len(lst_descend)):
            top_k.append(lst_descend[i][0])


    # REPLACE [] WITH A SUITABLE RETURN VALUE
    return top_k


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur *at least* min_count times

    Inputs:
        tokens: a list of tokens  (must be immutable)
        min_count: a non-negative integer

    Returns: set of tokens
    '''

    #Error checking (DO NOT MODIFY)
    if min_count < 0:
        raise ValueError("min_count must be a non-negative integer")

    # YOUR CODE HERE
    frequency = count_tokens(tokens)
    tokens_over_min_set = set()

    for entry in frequency:
        if frequency[entry] >= min_count:
            tokens_over_min_set.add(entry)
    

   

    # REPLACE set() WITH A SUITABLE RETURN VALUE
    return tokens_over_min_set


def compute_tf(t, d):
    word_frequency = count_tokens(d)

    tf = 0.5 + 0.5 * (word_frequency[t] / max(word_frequency.values()))

    return tf


def compute_idf(t, D):
    N = len(D)
    count_docs_with_t = 0

    for d in D:
        if t in d:
            count_docs_with_t += 1

    idf = math.log(N / count_docs_with_t)

    return idf


def compute_tf_idf(t, d, D):
    tf_idf = compute_tf(t, d) * compute_idf(t, D)
    
    return tf_idf


def find_salient(docs, threshold):
    '''
    Compute the salient words for each document.  A word is salient if
    its tf-idf score is strictly above a given threshold.

    Inputs:
      docs: list of list of tokens
      threshold: float

    Returns: list of sets of salient words
    '''

    lst_salients_per_doc = []

    for d in docs:
        salients_per_doc = set() 
        if d != {}:
            for t in d: 
                if compute_tf_idf(t, d, docs) > threshold:
                    salients_per_doc.add(t)
            lst_salients_per_doc.append(salients_per_doc)
        else:
            lst_salients_per_doc.append(salients_per_doc)
    
    return lst_salients_per_doc
                
