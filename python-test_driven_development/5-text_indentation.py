#!/usr/bin/python3
"""
Text Indentation Module

This module provides a function that prints text with 2 new lines
after each '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':' characters.

    Args:
        text (str): The text to format and print.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None: This function only prints the formatted text.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Special case: empty string or only whitespace
    if not text or text.isspace():
        return

    i = 0
    n = len(text)

    # Skip leading spaces
    while i < n and text[i] == ' ':
        i += 1

    while i < n:
        # If we hit a separator
        if text[i] in ".?:":
            print(text[i], end="")
            print("\n")
            i += 1

            # Skip all whitespace
            while i < n and text[i] in " \t\n":
                i += 1
        else:
            print(text[i], end="")
            i += 1
