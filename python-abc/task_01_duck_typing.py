#!/usr/bin/env python3
"""Shapes, interfaces, and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        ...
    
    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        ...


class Circle(Shape):
    """A circle shape."""
    
    def __init__(self, radius: float) -> None:
        """Initialize a circle with the given radius."""
        self.radius = radius
    
    def area(self) -> float:
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
    
    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        return 2.0 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle shape."""
    
    def __init__(self, width: float, height: float) -> None:
        """Initialize a rectangle with the given width and height."""
        self.width = width
        self.height = height
    
    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height
    
    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2.0 * (self.width + self.height)


def shape_info(shape) -> None:
    """
    Print the area and perimeter of a shape.
    
    This function uses duck typing - it assumes the shape object has
    area() and perimeter() methods.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
