def is_isogram(string):
    for word in string.split('\s'):
        d = {}
        for letter in list(word.lower()):
            if letter in d:
                return False
            else:
                d[letter] = ''
    return True
