from typing import Callable, NamedTuple


def divide(num1: float, num2: float) -> float:
    """
    returns num1 / num2
    :param float num1: number's numerator
    :param float num2: number's denominator
    :return float: returns num1 / num2
    :raise ValueError: if divides by 0
    """
    if num2 == 0:
        raise ValueError("division by 0 ")
    return num1 / num2


def factorial(num1: int) -> float:
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


def is_sign_minus(expression: str, index: int) -> bool:
    """
    returns if the symbol in index "index" is a sign minus
    :param str expression: a string the contains the expression
    :param int index: the index of the symbol to check
    :return: returns if the symbol in index "index" is a sign minus
    """
    char = expression[index]
    before_numeric = index != 0 and expression[index - 1].isnumeric()
    after_numeric = index < len(expression) - 1 and expression[index + 1] in "0123456789-"
    return char == '-' and not before_numeric and after_numeric


class Implied_operators(NamedTuple):
    priority: float
    inputs: int
    function: Callable[..., float]
    check_func: Callable[[str, int], bool]
    input_before: bool = True
    input_after: bool = True


IMPLIED_OPERATORS = {
    'S': Implied_operators(1, 1, lambda num1: -num1, is_sign_minus),
}


class Operator(NamedTuple):
    priority: float
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
OPERATORS.update(IMPLIED_OPERATORS)
