"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request
import re

DICTIONARY = os.path.join('/tmp', 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""
    word = re.sub(r'\W+', '', word).lower()
    for index, letter in enumerate(word):
        if word[index] == word[-index-1]:
            result = True
        else:
            result = False
            break
    return result


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""
    results = list()
    if words==None:
        words = load_dictionary()
    else:
        words = words
    if is_palindrome(words):
            results.append(words)
        else:
            continue
    return sorted(results, key=len)[0]