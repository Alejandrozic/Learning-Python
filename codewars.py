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
