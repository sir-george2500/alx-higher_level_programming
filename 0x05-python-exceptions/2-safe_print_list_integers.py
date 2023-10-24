#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Safely prints the first 'x' integers in 'my_list'.

    Args:
        my_list (list, optional): The list containing integers. Defaults to an empty list.
        x (int, optional): The number of integers to print. Defaults to 0.

    Returns:
        None
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            pass
    print()
    return

