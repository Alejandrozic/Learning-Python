"""
    My solutions to CodeWar challenges
"""

# -- KATA Disemvowel Trolls 7kyu
def disemvowel(string):
    return ''.join([c for c in string if c.lower() not in {'a','e','i','o','u'}])
