#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list (only once for each integer)."""
    unique_sum = 0
    seen = []  # Keep track of numbers we've already added

    for num in my_list:
        if num not in seen:
            unique_sum += num
            seen.append(num)
    return unique_sum
