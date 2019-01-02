"""
    Codewars Challenge
    An isogram is a word that has no repeating letters, 
    consecutive or non-consecutive. Implement a function 
    that determines whether a string that contains only 
    letters is an isogram. Assume the empty string is an
    isogram. Ignore letter case.
"""

def is_isogram(string):
    for word in string.split('\s'):
        d = {}
        for letter in list(word.lower()):
            if letter in d:
                return False
            else:
                d[letter] = ''
    return True
