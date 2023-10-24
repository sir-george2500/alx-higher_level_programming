#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    Safely prints the first 'x' elements of 'my_list'.

    Args:
        my_list (list): The list to be printed.
        x (int): The number of elements to print.

    Returns:
        None
    """
    num = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            num += 1
        except IndexError:
            break
    print("")
    return


