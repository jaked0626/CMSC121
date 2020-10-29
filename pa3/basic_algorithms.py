# Programming Assignment 3: Basic Algorithms

# Jake Underland

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

    Returns: 
        top_k: a list of the top k tokens ordered by count.
    '''

    #Error checking (DO NOT MODIFY)
    if k < 0:
        raise ValueError("In find_top_k, k must be a non-negative integer")
    
    # Convert given list into dictionary (frequency) listing tokens and 
    # their frequency in original list. Then, convert the dictionary into  
    # list (lst_frequency) of value pairs with token and its frequency 
    # paired as a tuple. Then, sort the list according to frequency and 
    # put them in a new list (lst_descend) in descending order. 

    frequency = count_tokens(tokens)
    lst_frequency = []

    for entry in frequency.items():
        lst_frequency.append(entry)

    lst_descend = sort_count_pairs(lst_frequency)

    # Add first k tokens in lst_descend to new list (top_k), treating 
    # the case where k > len(lst_descend) specially. 
    
    top_k = []

    if k <= len(lst_descend):
        for i in range(k):
            top_k.append(lst_descend[i][0])
    else:
        for i, _ in enumerate(lst_descend):
            top_k.append(lst_descend[i][0])

    return top_k


def find_min_count(tokens, min_count):
    '''
    Find the tokens that occur *at least* min_count times

    Inputs:
        tokens: a list of tokens  (must be immutable)
        min_count: a non-negative integer

    Returns: 
        tokens_over_min_set: list of tokens that occur more 
            than the given minimum threshold.
    '''

    #Error checking (DO NOT MODIFY)
    if min_count < 0:
        raise ValueError("min_count must be a non-negative integer")

    # Convert list of tokens into dictionary with tokens as key and 
    # number of apppearances of token in list as value. for each key
    # in the dictionary, if the value exceeds min_count, add to final set.

    frequency = count_tokens(tokens) 
    tokens_over_min_set = set()

    for entry in frequency:
        if frequency[entry] >= min_count:
            tokens_over_min_set.add(entry)
    

    return tokens_over_min_set


def compute_tf(t, d):
    '''
    Computes the augmented freqeuncy of a term t in a document d. 

    Inputs:
        t: a term (immutable)
        d: document that the term belongs to (list of tokens)

    Returns: 
        tf: augmented frequency of the term (float)
    '''

    # divide frequency of term t by the frequency of the most frequent
    # term in document d, and applies that to the formula for term frequency.

    word_frequency = count_tokens(d)

    tf = 0.5 + 0.5 * (word_frequency[t] / max(word_frequency.values()))

    return tf


def compute_idf(t, D):
    '''
    Computes the inverse document frequency of a term t in a 
    corpus (collection of documents) D. 

    Inputs:
        t: a term (immutable)
        D: document that the term belongs to (list of list of tokens)

    Returns: 
        idf: inverse document frequency (float)
    '''

    N = len(D)
    count_docs_with_t = 0

    for d in D:
        if t in d:
            count_docs_with_t += 1

    idf = math.log(N / count_docs_with_t)

    return idf


def compute_tf_idf(t, d, D):
    '''
    Computes the term frequency-inverse document frequency of a token t
    in document d, in a collection of documents D. 

    Inputs:
        t: a term (immutable)
        d: a document (list of tokens)
        D: document that the term belongs to (list of list of tokens)

    Returns: 
        tf_idf: term frequency-inverse document frequency (float)
    '''

    tf_idf = compute_tf(t, d) * compute_idf(t, D)
    
    return tf_idf


def find_salient(docs, threshold):
    '''
    Compute the salient words for each document. A word is salient if
    its tf-idf score is strictly above a given threshold.

    Inputs:
        docs: list of list of tokens
        threshold: float

    Returns: 
        lst_salients_per_doc: list of sets of salient words
    '''

    lst_salients_per_doc = []  # list of sets of salient words per doc

    for d in docs:

        salients_per_doc = set()  # compute set of salient words per doc

        if d != {}:

            for t in d: 
                if compute_tf_idf(t, d, docs) > threshold:  # if word is salient
                    salients_per_doc.add(t)

            # append set of salient words to list of sets        
            lst_salients_per_doc.append(salients_per_doc)  

        else:  # if document is empty
            lst_salients_per_doc.append(salients_per_doc)  
            # append empty set (no salient words)
    
    return lst_salients_per_doc
                
