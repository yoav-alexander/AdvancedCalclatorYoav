import math

"""
this module includes all the necessary
function to run operations for the calculator
"""


def divide(num1: float, num2: float) -> float:
    """
    returns num1 / num2
    :param float num1: number's numerator
    :param float num2: number's denominator
    :return float: returns num1 / num2
    :raise ArithmeticError: if divides by 0
    """
    if num2 == 0:
        raise ArithmeticError(f"invalid division by 0: {num1:g}/{num2:g}")
    return num1 / num2


def factorial(num1: int) -> float:
    """
    returns the factorial of the given number
    :param num1: a whole non-negative number
    :return int: returns the factorial of the given number
    :raise ArithmeticError: num1 < 0 or not whole
    """
    if num1 % 1 != 0 or num1 < 0:
        raise ArithmeticError(f"invalid input: factorial operation is only valid for positive integers: {num1:g}! ")

    result = 1.0
    for i in range(1, int(num1) + 1):
        result *= i

    if result == float("inf"):
        raise OverflowError("result too large")
    return result


def power(base: float, exponent: float) -> float:
    """
    returns base to the power of exponent
    :param float base: operator's base
    :param float exponent: Operator's exponent
    :return float: returns base to the power of exponent
    :raise ArithmeticError: if invalid
    """
    if base == exponent == 0:
        raise ArithmeticError(f"invalid input for power operation: {base:g}^{exponent:g}")
    try:
        return math.pow(base, exponent)
    except (ValueError, OverflowError):
        raise ArithmeticError(f"invalid input for power operation: {base:g}^{exponent:g}")


def digit_sum(num1: float) -> float:
    """
    returns the sum of the given number's digits
    :param float num1: a positive number
    :return: returns the sum of the given number's digits
    :raise ArithmeticError: if given negative number
    """
    if num1 < 0:
        raise ArithmeticError(f"invalid input: digit sum operation is invalid for negative numbers: {num1}")
    return sum(float(digit) for digit in str(f"{num1:f}") if digit.isdigit())
