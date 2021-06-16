def repeated_word(text: str) -> str:
    """Return first repeated word in the given text. If all words are unique returns None

    Args:
        text (str): Given text
    Raises:
        TypeError: If the passed in text is not a string
    Returns:
        str: First repeated word
    """
    if not type(text) is str:
        raise TypeError('text must be a string!')

    text_lst = text.split(' ')
    existing_words = set()

    for word in text_lst:
        word = ''.join(char for char in word if char. isalnum()).lower()
        if word in existing_words:
            return word
        else:
            existing_words.add(word)

    return None
