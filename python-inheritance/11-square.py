#!/usr/bin/python3
"""Defines a Square class with a custom string representation."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square defined by a validated private size."""

    def __init__(self, size):
        """Initialize a Square with a validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the string representation: [Square] <size>/<size>."""
        return "[Square] {0}/{0}".format(self.__size)
