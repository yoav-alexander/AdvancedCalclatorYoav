from typing import Callable, NamedTuple


def factorial(num1: int) -> int:
    # check if whole number and positive
    if num1 in [0, 1]:
        return 1
    return num1 * factorial(num1 - 1)


class Operator(NamedTuple):
    priority: int
    inputs: int
    function: Callable[..., float]


OPERATORS = {
    '+': Operator(1, 2, lambda num1, num2: num1 + num2),
    '-': Operator(1, 2, lambda num1, num2: num1 - num2),
    '*': Operator(2, 2, lambda num1, num2: num1 * num2),
    '/': Operator(2, 2, lambda num1, num2: num1 / num2),
    '^': Operator(3, 2, lambda num1, num2: num1 ** num2),
    '@': Operator(5, 2, lambda num1, num2: (num1 / num2) / 2),
    '$': Operator(5, 2, lambda num1, num2: max(num1, num2)),
    '&': Operator(5, 2, lambda num1, num2: min(num1, num2)),
    '%': Operator(4, 2, lambda num1, num2: num1 % num2),
    '~': Operator(6, 1, lambda num1: -num1),
    '!': Operator(6, 1, factorial),
}
