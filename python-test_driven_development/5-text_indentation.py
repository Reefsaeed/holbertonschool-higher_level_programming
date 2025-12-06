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

    if not text:
        return

    i = 0
    length = len(text)

    # Skip leading spaces
    while i < length and text[i] == ' ':
        i += 1

    while i < length:
        print(text[i], end="")

        if text[i] in ".?:":
            print("\n")
            i += 1

            # Skip all whitespace after separator
            while i < length and text[i] == ' ':
                i += 1
            continue

        i += 1
