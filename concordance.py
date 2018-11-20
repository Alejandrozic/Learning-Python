from re import sub


def concordence(text):
    """
    Word Count

    :param text:    string
    :return:        dict
    """
    freq = {}

    for word in text.split():

        word = sub('[^\w]', '', word.lower())

        if word not in freq:
            freq[word] = 0

        freq[word] += 1

    return freq
