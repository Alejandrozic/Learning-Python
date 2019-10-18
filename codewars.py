"""
    My solutions to CodeWar challenges
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
