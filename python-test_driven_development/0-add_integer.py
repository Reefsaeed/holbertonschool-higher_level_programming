#!/usr/bin/python3
"""
This module provides a function to add two integers.
The function handles both integers and floats by casting floats to integers.

It demonstrates proper error handling for edge cases.
This includes handling infinity and NaN values.
"""


def add_integer(a, b=98):
    """
    Add two integers.
    
    Args:
        a: First number (int or float)
        b: Second number (int or float), defaults to 98
    
    Returns:
        int: The sum of a and b as an integer
    
    Raises:
        TypeError: If a or b is not an integer or float
    
    Examples:
        >>> add_integer(1, 2)
        3
        >>> add_integer(100, -2)
        98
        >>> add_integer(2)
        100
        >>> add_integer(100.3, -2)
        98
    """
    # Check if a is integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is integer or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to integers
    try:
        a = int(a)
        b = int(b)
    except (OverflowError, ValueError) as e:
        # Re-raise to ensure exact message
        raise type(e)(str(e))

    # Return the sum
    return a + b
