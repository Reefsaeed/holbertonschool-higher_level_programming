#!/usr/bin/python3
def multiple_returns(sentence):
    """Returns a tuple with length of string and its first character."""
    if len(sentence) == 0:
        return (0, None)
    return (len(sentence), sentence[0])
