"""
    ###################################
     My solutions to CodeWar challenges
    ###################################
"""

# -- KATA Disemvowel Trolls 7kyu
def disemvowel(string):
    return ''.join([c for c in string if c.lower() not in {'a','e','i','o','u'}])

# -- KATA Categorize New Member 7kyu
def openOrSenior(data):
    output = list()
    for person in data:
        age, handicap = person[0], person[1]
        output.append('Senior' if age > 54 and handicap > 7 else 'Open')
    return output

# -- KATA Find the next perfect square! 7kyu
def find_next_square(sq):
    n = sq**0.5
    return -1 if n % 1 else (n+1) **2

"""
KATA Ones and Zeros 7kyu

Given an array of ones and zeroes, convert the equivalent binary value to an integer.
Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
"""
def binary_array_to_number(arr):
    sum_ = 0
    while arr:
        binary, exponent = arr.pop(0), len(arr)
        sum_ += binary * (2 ** exponent)
    return sum_

"""
KATA Find the missing letter 6kyu

Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter in the array.
You will always get an valid array. And it will be always exactly one letter be missing. The length of the array will always be at least 2.
The array will always contain letters in only one case.
"""
import string
def find_missing_letter(chars):
    if chars[0].islower():
        alphabet = string.ascii_lowercase
    else:
        alphabet = string.ascii_uppercase
    alphabet = alphabet[
               alphabet.index(chars[0]):
               alphabet.index(chars[-1])+1
               ]
    return list(set(alphabet) - set(chars))[0]
