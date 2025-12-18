#!/usr/bin/env python3
"""
Test file for the duck typing exercise
Demonstrates the usage of Circle, Rectangle, and shape_info function
"""

from task_01_duck_typing import Circle, Rectangle, shape_info

if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    # Test the shape_info function with both shapes
    shape_info(circle)
    shape_info(rectangle)
