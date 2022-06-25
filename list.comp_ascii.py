def get_word_codes(words):
    """Given a list of words, return a dictionary where the words are keys,
    and the value for each key is a list of the character codes of the
    letters of the word that is its key."""
    return {word:[ord(x) for x in word] for word in words}

get_word_codes =
print(get_word_codes(upper(["this", "is", "a", "list", "of", "words"])))