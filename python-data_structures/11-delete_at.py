#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Deletes the item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list

    # Create new list without the element at index idx
    new_list = []
    for i in range(len(my_list)):
        if i != idx:
            new_list.append(my_list[i])
    return new_list
