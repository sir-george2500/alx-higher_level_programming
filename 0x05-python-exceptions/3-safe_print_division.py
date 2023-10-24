#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Safely performs division of two numbers.

    Args:
        a (int, float): The dividend.
        b (int, float): The divisor.

    Returns:
        float or None: The result of the division, or None in case of division by zero.
    """
    try:
        div = a / b
    except ZeroDivisionError:
        div = None
    finally:
        print("Inside result: {}".format(div))
        return div
