from typing import Callable, NamedTuple


def divide(num1: float, num2: float) -> float:
    """
    returns num1 / num2
    :param float num1: number's numerator
    :param float num2: number's denumerator
    :return float: returns num1 / num2
    :raise ValueError: if divides by 0
    """
    if num2 == 0:
        raise ValueError("division by 0 ")
    return num1 / num2


def factorial(num1: float) -> float:
    """
    returns the factorial of the given number
    :param num1: a whole non-negative number
    :return int: returns the factorial of the given number
    :raise ValueError: num1 < 0 or not whole
    """
    if num1 < 0 or num1 % 1 != 0:
        raise ValueError(f"invalid input for factorial operation: {num1}! ")
    # check if whole number and positive
    if num1 in [0, 1]:
        return 1
    return num1 * factorial(num1 - 1)


def power(base: float, exponent: float) -> float:
    """
    returns base to the power of exponent
    :param float base: operator's base
    :param float exponent: Operator's exponent
    :return float: returns base to the power of exponent
    :raise ValueError: if 0^0
    """
    if base == exponent == 0:
        raise ValueError(f"invalid input for power operation: 0^0! ")
    return base ** exponent


class Operator(NamedTuple):
    priority: int
    inputs: int
    function: Callable[..., float]
    input_before: bool = True
    input_after: bool = True


OPERATORS = {
    '+': Operator(1, 2, lambda num1, num2: num1 + num2),
    '-': Operator(1, 2, lambda num1, num2: num1 - num2),
    '*': Operator(2, 2, lambda num1, num2: num1 * num2),
    '/': Operator(2, 2, divide),
    '^': Operator(3, 2, power),
    '@': Operator(5, 2, lambda num1, num2: (num1 / num2) / 2),
    '$': Operator(5, 2, lambda num1, num2: max(num1, num2)),
    '&': Operator(5, 2, lambda num1, num2: min(num1, num2)),
    '%': Operator(4, 2, lambda num1, num2: num1 % num2),
    '~': Operator(6, 1, lambda num1: -num1, input_before=False),
    '!': Operator(6, 1, factorial, input_after=False)
}
