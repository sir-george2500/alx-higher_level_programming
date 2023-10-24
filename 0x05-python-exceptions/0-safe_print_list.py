#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first 'x' elements of 'my_list'.

    Args:
        my_list (list, optional): The list to be printed. Defaults to an empty list.
        x (int, optional): The number of elements to print. Defaults to 0.

    Returns:
        int: The total number of elements printed.
    """
    total = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            total += 1
        except IndexError:
            break
    print()
    return total

