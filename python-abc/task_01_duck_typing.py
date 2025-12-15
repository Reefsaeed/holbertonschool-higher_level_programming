#!/usr/bin/env python3
"""
Shapes, Interfaces, and Duck Typing
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes
    """
    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter
        """
        pass


class Circle(Shape):
    """
    Circle class inheriting from Shape
    """
    def __init__(self, radius):
        """
        Initialize circle with radius
        """
        self.radius = radius

    def area(self):
        """
        Calculate area of circle
        Formula: π * r^2
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate perimeter (circumference) of circle
        Formula: 2 * π * r
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class inheriting from Shape
    """
    def __init__(self, width, height):
        """
        Initialize rectangle with width and height
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate area of rectangle
        Formula: width * height
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate perimeter of rectangle
        Formula: 2 * (width + height)
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape
    Uses duck typing - assumes shape has area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
