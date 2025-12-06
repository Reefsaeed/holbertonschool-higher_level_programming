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
    n = len(text)

    # Skip leading spaces
    while i < n and text[i] == ' ':
        i += 1

    while i < n:
        # Check if current char is separator
        if text[i] in ".?:":
            print(text[i], end="")

            # Check if we have consecutive separators
            j = i + 1
            has_consecutive = False
            while j < n and text[j] in ".?:":
                has_consecutive = True
                print(text[j], end="")
                j += 1

            # Only add new lines if NOT followed by another separator
            if not has_consecutive:
                print("\n")

                # Skip ALL whitespace (spaces, tabs, newlines)
                j = i + 1
                while j < n and text[j] in " \t\n":
                    j += 1

                i = j
                continue
            else:
                # We already printed all consecutive separators
                i = j
                continue

        print(text[i], end="")
        i += 1
