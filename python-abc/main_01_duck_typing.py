#!/usr/bin/env python3
"""Test file for duck typing shapes."""
from task_01_duck_typing import Circle, Rectangle, shape_info

print("Testing Circle with radius=5:")
circle = Circle(radius=5)
print("Circle created")
print("Circle area:", circle.area())
print("Circle perimeter:", circle.perimeter())
print()

print("Testing Rectangle with width=4, height=7:")
rectangle = Rectangle(width=4, height=7)
print("Rectangle created")
print("Rectangle area:", rectangle.area())
print("Rectangle perimeter:", rectangle.perimeter())
print()

print("Testing shape_info with Circle:")
shape_info(circle)
print()

print("Testing shape_info with Rectangle:")
shape_info(rectangle)
