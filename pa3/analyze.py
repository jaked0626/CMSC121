"""
Analyze module
"""

import unicodedata
import sys

from basic_algorithms import find_top_k, find_min_count, find_salient

##################### DO NOT MODIFY THIS CODE #####################

def keep_chr(ch):
    '''
    Find all characters that are classifed as punctuation in Unicode
    (except #, @, &) and combine them into a single string.
    '''
    return unicodedata.category(ch).startswith('P') and \
        (ch not in ("#", "@", "&"))

PUNCTUATION = " ".join([chr(i) for i in range(sys.maxunicode)
                        if keep_chr(chr(i))])

# When processing tweets, ignore these words
STOP_WORDS = ["a", "an", "the", "this", "that", "of", "for", "or",
              "and", "on", "to", "be", "if", "we", "you", "in", "is",
              "at", "it", "rt", "mt", "with"]

# When processing tweets, words w/ a prefix that appears in this list
# should be ignored.
STOP_PREFIXES = ("@", "#", "http", "&amp")


#####################  MODIFY THIS CODE #####################


############## Part 2 ##############

# Task 2.1


def convert_items_in_entities_to_lst(tweets, entity_desc):
    '''
    Given a list of tweets, constructs a list from specified
    entity and subkey of each tweet, converting the case of 
    each element as specified. 

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
        k: integer

    Returns: 
        lst_entity: list of all entities in collection of tweets.
    '''

    entity, subkey, case = entity_desc
    lst_entity = []

    for tweet in tweets:

        for item in tweet['entities'][entity]:

            if case:
                lst_entity.append(item[subkey])
            else: 
                lst_entity.append(item[subkey].lower())

    return lst_entity


def find_top_k_entities(tweets, entity_desc, k):
    '''
    Find the k most frequently occuring entitites

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
        k: integer

    Returns: 
        top_k_lst: list of top k frequentyly occuring entities
    '''
    
    # convert tweets into one long list of entities using helper function
    # and run find_top_k

    lst_entity = convert_items_in_entities_to_lst(tweets, entity_desc)
    
    top_k_lst = find_top_k(lst_entity, k)

    return top_k_lst


# Task 2.2
def find_min_count_entities(tweets, entity_desc, min_count):
    '''
    Find the entitites that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        entity_desc: a triple ("hashtags", "text", True),
          ("user_mentions", "screen_name", False), etc
        min_count: integer

    Returns: set of entities
    '''

    # convert tweets into one long list of entities using helper function
    # and run find_min_count
    
    lst_entity = convert_items_in_entities_to_lst(tweets, entity_desc)
    
    min_count_set = find_min_count(lst_entity, min_count)

    return min_count_set




############## Part 3 ##############


def convert_tweet_lst(tweet):
    '''
    Takes a tweet and converts its abridged text into a list of 
    words (separated by spaces). 

    Inputs:
        tweet: dictionary

    Returns: 
        total_words_lst: list of words
    '''

    total_words_lst = []

    word_lst = tweet["abridged_text"].split()

    for word in word_lst:
        if word != "":  # Do not add empty spaces as words
            total_words_lst.append(word)

    return total_words_lst

def remove_punctuation(total_words_lst):
    '''
    Takes a list of words and removes punctuation around word. 

    Inputs:
        total_words_lst: list of words

    Returns: 
        new_list: list of words with punctuation removed
    '''

    new_list = []

    for word in total_words_lst:

        stripped = word.strip(PUNCTUATION)  # remove puntuation front and back

        if stripped != "":  # do not add empty spaces as words
            new_list.append(stripped)

    return new_list

def convert_to_lower(total_words_lst):
    '''
    Takes a list of words and converts words into lower case. 

    Inputs:
        total_words_lst: list of words

    Returns: 
        new_lst: list of words in lower case
    '''

    new_lst = []

    for word in total_words_lst:

        new_lst.append(word.lower())  # add words in lwoer case form

    return new_lst

def remove_stop_words(total_words_lst):
    '''
    Takes a list of words and removes STOPWORDS from list. 

    Inputs:
        total_words_lst: list of words

    Returns: 
        new_lst: list of words with stopwords removed
    '''

    new_lst = []

    for word in total_words_lst:

        if word not in STOP_WORDS:  # Do not append words in STOP_WORDS
            new_lst.append(word)

    return new_lst


def remove_prefixes(total_words_lst):
    '''
    Takes a list of words and removes words with certain prefixes. 

    Inputs:
        total_words_lst: list of words

    Returns: 
        new_list: list of words with certain words with prefixes removed
    '''

    new_list = []

    for word in total_words_lst:

        if not word.startswith(STOP_PREFIXES):  
            # Do not append words with STOP_PREFIXES
            new_list.append(word)

    return new_list


def preprocess(tweet, eliminate_stop, case_sensitive):
    '''
    Preprocesses a tweet and returns a list of words treated
    according to the stipulations.  

    Inputs:
        tweet: dictionary
        eliminate_stop: boolean, True if eliminating STOP_WORDS
        case_sensitive: boolean, True if case sensitive distinction of words.

    Returns: 
        lst: list of words from tweet preprocessed
    '''

    lst = convert_tweet_lst(tweet)  # extract text from tweet

    lst = remove_punctuation(lst)  # remove punctuation

    if not case_sensitive:  # convert to lower case not case sensitive
        lst = convert_to_lower(lst)

    if eliminate_stop:  # eliminate stop_words if analysis requires it
        lst = remove_stop_words(lst)

    lst = remove_prefixes(lst)  # remove words that start with prefix from lst

    return lst


def create_ngram_lst(tweet, n, case_sensitive, eliminate_stop):
    '''
    Creates a list of ngrams out of extracted text from tweet. 

    Inputs:
        tweet: dictionary
        n: integer, specifies how many words ngrams will comprise
        case_sensitive: boolean, True if case sensitive distinction of words
        eliminate_stop: boolean, True if analysis requires removal of STOP_WORDS

    Returns: 
        ngrams: list of ngrams
    '''

    ngrams = []

    # preprocess text in tweet and yield list of words
    words_in_tweet = preprocess(tweet, eliminate_stop, case_sensitive)

    for i, _ in enumerate(words_in_tweet):

        if i+n <= len(words_in_tweet):  # ngrams do not spill over
            n_gram = tuple(words_in_tweet[i:i+n])
            ngrams.append(n_gram)  # list of tuples, each containing ngram

    return ngrams


def find_top_k_ngrams(tweets, n, case_sensitive, k):
    '''
    Find k most frequently occurring n-grams

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        k: integer

    Returns: 
        top_k_n: list of n-grams
    '''

    n_grams_lst = []

    # create list of ngrams for each tweet and combine 
    # into one long list (n_grams_lst).

    for tweet in tweets:
        n_grams_lst += create_ngram_lst(tweet, n, case_sensitive, True)
    
    top_k_n = find_top_k(n_grams_lst, k)
    
    return top_k_n


def find_min_count_ngrams(tweets, n, case_sensitive, min_count):
    '''
    Find n-grams that occur at least min_count times.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        min_count: integer

    Returns: set of n-grams
    '''
    n_grams_lst = []

    # create list of ngrams for each tweet and 
    # combine into one long list (n_grams_lst).
    
    for tweet in tweets:
        n_grams_lst += create_ngram_lst(tweet, n, case_sensitive, True)

    min_ngrams = find_min_count(n_grams_lst, min_count)
    
    return min_ngrams

def find_salient_ngrams(tweets, n, case_sensitive, threshold):
    '''
    Find the salient n-grams for each tweet.

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        threshold: float

    Returns: list of sets of strings
    '''

    series_of_ngrams = []

    # create list of lists of ngrams per tweet

    for tweet in tweets:

        ngrams = create_ngram_lst(tweet, n, case_sensitive, False) 
        series_of_ngrams.append(ngrams)

    salient_ngrams = find_salient(series_of_ngrams, threshold)

    return salient_ngrams
