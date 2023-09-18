"""
    This module contains the basic math functions
"""


def add(num1, num2):
    """
        This function returns the add of two numbers
    """
    return num1 + num2


def sub(num1, num2):
    """
        This function returns the sub of two numbers
    """
    return num1 - num2


def mul(num1, num2):
    """
        This function returns the mul of two numbers
    """
    return num1 * num2


def div(num1, num2):
    """
        This function returns the div of two numbers
        If num2 is zero, it raises num1 ValueError exception
    """
    if num2 == 0:
        raise ValueError("Can't divide by zero")
    return num1 / num2


def mod(num1, num2):
    """
        This function returns the mod of two numbers
        If num2 is zero, it raises num1 ValueError exception
    """
    if num2 == 0:
        raise ValueError("Can't divide by zero")
    return num1 % num2


def count_in_list(iterable, elem):
    """
        Count in list
    """
    return len([x for x in iterable if x == elem])