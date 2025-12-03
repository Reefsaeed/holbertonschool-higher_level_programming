#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces element in list at position without modifying original."""
    if idx < 0 or idx >= len(my_list):
        return my_list[:]  # Return a copy, not the original
    new_list = my_list[:]  # Create a copy of the original list
    new_list[idx] = element  # Modify the copy
    return new_list
