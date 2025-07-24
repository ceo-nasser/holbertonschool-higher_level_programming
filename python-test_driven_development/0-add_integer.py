#!/usr/bin/python3
"""Defines a function that adds two integers.
    The function takes two arguments, a and b, and returns their sum.
    If either argument is not an integer or a float, a TypeError is raised.
    If either argument is a float, it is converted to an integer before addition.
    The default value of b is 98.
""" 
def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add. Defaults to 98.   
        Raises:
            TypeError: If either a or b is not an integer or a float.
    Returns:
        int: The sum of a and b, converted to an integer.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
