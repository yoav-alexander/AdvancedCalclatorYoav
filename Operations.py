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
        raise ArithmeticError("division by 0 ")
    return num1 / num2


def factorial(num1: int) -> float:
    """
    returns the factorial of the given number
    :param num1: a whole non-negative number
    :return int: returns the factorial of the given number
    :raise ArithmeticError: num1 < 0 or not whole
    """
    if num1 < 0 or num1 % 1 != 0:
        raise ArithmeticError(f"invalid input for factorial operation: {num1}! ")
    # check if whole number and positive
    if num1 in [0, 1]:
        return 1.0
    return num1 * factorial(num1 - 1)


def power(base: float, exponent: float) -> float:
    """
    returns base to the power of exponent
    :param float base: operator's base
    :param float exponent: Operator's exponent
    :return float: returns base to the power of exponent
    :raise ArithmeticError: if invalid
    """
    if base == exponent == 0 or -1 < exponent < 1 and base < 0:
        raise ArithmeticError(f"invalid input for power operation: {base}^{exponent} ")
    return base ** exponent


def digit_sum(num1: float) -> float:
    """
    returns the sum of the given number's digits
    :param float num1: a positive number
    :return: returns the sum of the given number's digits
    :raise ArithmeticError: if given negative number
    """
    if num1 < 0:
        raise ArithmeticError(f"invalid input for digit sum operation: {num1}")
    return sum(float(digit) for digit in str(num1) if digit.isnumeric())

