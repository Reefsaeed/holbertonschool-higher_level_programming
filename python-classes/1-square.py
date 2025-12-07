#!/usr/bin/python3
"""
Module 1-square
Defines a class Square with a private size attribute.
"""


class Square:
    """
    Class that defines a square.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
