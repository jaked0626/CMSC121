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

    Returns: list of entities
    '''

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
    
    lst_entity = convert_items_in_entities_to_lst(tweets, entity_desc)
    
    min_count_set = find_min_count(lst_entity, min_count)

    # REPLACE set() WITH A SUITABLE RETURN VALUE
    return min_count_set




############## Part 3 ##############


def convert_lst_words(tweets):

    total_words_lst = []

    for tweet in tweets:
        word_lst = tweet["abridged_text"].split(" ")
        for word in word_lst:
            if len(word) > 0:
                total_words_lst.append(word)
        #total_words_lst += word_lst

    return total_words_lst

def remove_punctuation(total_words_lst):
    new_list = []
    for word in total_words_lst:
        stripped = word.strip(PUNCTUATION)
        if stripped != "":
            new_list.append(stripped)


    return new_list

#def remove_punctuation(total_words_lst):

    new_lst = []

    for word in total_words_lst:

        if len(word) > 0:

            while word[0] in PUNCTUATION:
                # deletes first character in string until
                # first character is not a punctuation, or 
                # all characters are deleted.
                word = word[1:]
                if word == "":
                    break

            if word != "":
                while word[-1] in PUNCTUATION:
                    word = word[:-1]

                new_lst.append(word)

    return new_lst

def clean_data(tweets, eliminate_stop, case_sensitive):

    lst = convert_lst_words(tweets)
    new_lst = remove_punctuation(lst)
    newer_lst = []
    #for word in new_lst:
        #if 





#if word[0] in SOTP_PREFIXES:
#   lst.remove(word)



def find_top_k_ngrams(tweets, n, case_sensitive, k):
    '''
    Find k most frequently occurring n-grams

    Inputs:
        tweets: a list of tweets
        n: integer
        case_sensitive: boolean
        k: integer

    Returns: list of n-grams
    '''

    # YOUR CODE HERE

    # REPLACE [] WITH A SUITABLE RETURN VALUE
    return []



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

    # YOUR CODE HERE

    # REPLACE () WITH A SUITABLE RETURN VALUE
    return set()

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

    # YOUR CODE HERE

    # REPLACE [] WITH A SUITABLE RETURN VALUE
    return []
