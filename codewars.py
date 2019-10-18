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

"""
KATA Bouncing Balls 6kyu

A child is playing with a ball on the nth floor of a tall building. The height of this floor, h, is known.
He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).
His mother looks out of a window 1.5 meters from the ground.
How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing?
Three conditions must be met for a valid experiment:
Float parameter "h" in meters must be greater than 0
Float parameter "bounce" must be greater than 0 and less than 1
Float parameter "window" must be less than h.
If all three conditions above are fulfilled, return a positive integer, otherwise return -1.
"""

def bouncingBall(h, bounce, window):
    if 0 < bounce < 1 and 0 < h < window:
        return -1
    count = 0
    while h >= window:
        # Fall
        count += 1
        # Contact with Floor
        h = h * bounce
        # Rise
        if h >= window:
            count += 1
    return count
