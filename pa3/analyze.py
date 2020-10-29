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

#def convert_lst_words(tweets):

    #total_words_lst = []

    #for tweet in tweets:
        #word_lst = tweet["abridged_text"].split(" ")
        #for word in word_lst:
            #if word != "":
                #total_words_lst.append(word)

    #return total_words_lst

def convert_tweet_lst(tweet):

    total_words_lst = []
    word_lst = tweet["abridged_text"].split()
    for word in word_lst:
        if word != "":
            total_words_lst.append(word)

    return total_words_lst

def remove_punctuation(total_words_lst):

    new_list = []
    for word in total_words_lst:
        stripped = word.strip(PUNCTUATION)
        if stripped != "":
            new_list.append(stripped)

    return new_list

def convert_to_lower(total_words_lst):
    new_lst = []
    for word in total_words_lst:
        new_lst.append(word.lower())

    return new_lst

def remove_stop_words(total_words_lst):

    new_lst = []
    for word in total_words_lst:
        if word not in STOP_WORDS:
            new_lst.append(word)

    return new_lst

def remove_prefixes(total_words_lst):
    new_list = []
    for word in total_words_lst:
        if word.startswith(STOP_PREFIXES) == False:
            new_list.append(word)

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

def clean_data(tweet, eliminate_stop, case_sensitive):
    lst = convert_tweet_lst(tweet)
    lst = remove_punctuation(lst)
    if case_sensitive == False:
        lst = convert_to_lower(lst)
    if eliminate_stop:
        lst = remove_stop_words(lst)
    lst = remove_prefixes(lst)

    return lst

#def    lst = convert_tweet_lst(tweet)
    lst = remove_punctuation(lst)
    lst = remove_prefixes(lst)
    new_list = []

    for word in lst:
        if case_sensitive:
            if eliminate_stop:
                if word not in STOP_WORDS:
                    new_list.append(word)
            else:
                new_list.append(word)
        else:
            if eliminate_stop:
                if word.lower() not in STOP_WORDS:
                    new_list.append(word.lower())
            else:
                new_list.append(word.lower())

    return new_list


        #if word.startswith(STOP_PREFIXES) == False:
            #new_lst.append(word)

    #for word in newer_lst: 
        #if eliminate_stop:
            #if word in STOP_WORDS:
                #newer_lst.remove(word)
    
    #if case_sensitive == False:
        #newer_lst = lower(newer_lst)
    
    #return newer_lst

def create_ngram_lst(tweet, n, case_sensitive, eliminate_stop):
    ngrams = []
    words_in_tweet = clean_data(tweet, eliminate_stop, case_sensitive)
    for i, word in enumerate(words_in_tweet):
        if i+n <= len(words_in_tweet):
            n_gram = tuple(words_in_tweet[i:i+n])
            ngrams.append(n_gram)
    return ngrams


def create_ngrams_lst(tweets, n, case_sensitive):
    n_grams_lst = []
    for tweet in tweets:
        words_in_tweet = clean_data(tweet, True, case_sensitive)
        for i, word in enumerate(words_in_tweet):
            if i+n <= len(words_in_tweet):
                n_gram = tuple(words_in_tweet[i:i+n])
                n_grams_lst.append(n_gram)
    return n_grams_lst

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
    n_grams_lst = create_ngrams_lst(tweets, n, case_sensitive)
    
    top_k_n = find_top_k(n_grams_lst, k)
    
    return top_k_n

#def words_in_tweets = clean_data(tweets, True, case_sensitive)
    for i, word in enumerate(words_in_tweets):
        if i+n <= len(words_in_tweets):
            n_gram = tuple(words_in_tweets[i:i+n])
            n_grams_lst.append(n_gram)
        #else: 
            #n_gram = tuple(words_in_tweets[i:])
            #n_grams_lst.append(n_gram)
    
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
    n_grams_lst = create_ngrams_lst(tweets, n, case_sensitive)
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
    for tweet in tweets:
        ngrams = create_ngram_lst(tweet, n, case_sensitive, False)
        series_of_ngrams.append(ngrams)

    salient_ngrams = find_salient(series_of_ngrams, threshold)

    return salient_ngrams
