#!/usr/bin/env python3
"""
Duck Typing Exercise
This module demonstrates duck typing and abstract base classes
in Python by implementing shapes with area and perimeter calculations.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape"""

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape"""


class Circle(Shape):
    """Circle class that inherits from Shape"""

    def __init__(self, radius):
        """Initialize a circle with given radius"""
        self.radius = radius

    def area(self):
        """Calculate area of circle: π * r^2"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate perimeter (circumference) of circle: 2 * π * r"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class that inherits from Shape"""

    def __init__(self, width, height):
        """Initialize a rectangle with given width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate area of rectangle: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Calculate perimeter of rectangle: 2 * (width + height)"""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing

    Args:
        shape: Any object that has area() and perimeter() methods
    """
    # Duck typing in action - we just call the methods
    # without checking the type
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
