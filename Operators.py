from typing import Callable
from Operations import divide, power, digit_sum, factorial


class Operator:
    """
    A class that represent an Operator

    Attributes:
        priority: float
        inputs: int
        function: Callable[..., float]
        input_before: bool = True
        input_after: bool = True
    """

    def __init__(self,
                 symbol: str,
                 priority: float,
                 inputs: int,
                 function: Callable[..., float],
                 input_before: bool = True,
                 input_after: bool = True):
        self.symbol = symbol
        self.priority = priority
        self.inputs = inputs
        self.function = function
        self.input_before = input_before
        self.input_after = input_after


OPERATORS = {
    '+': Operator('+', 1, 2, lambda num1, num2: num1 + num2),
    '-': Operator('-', 1, 2, lambda num1, num2: num1 - num2),
    '*': Operator('*', 2, 2, lambda num1, num2: num1 * num2),
    '/': Operator('/', 2, 2, divide),
    '^': Operator('^', 3, 2, power),
    '%': Operator('%', 4, 2, lambda num1, num2: num1 % num2),
    '@': Operator('@', 5, 2, lambda num1, num2: (num1 + num2) / 2),
    '$': Operator('$', 5, 2, lambda num1, num2: max(num1, num2)),
    '&': Operator('&', 5, 2, lambda num1, num2: min(num1, num2)),
    '~': Operator('~', 6, 1, lambda num1: -num1, input_before=False),
    '#': Operator('#', 6, 1, digit_sum, input_after=False),
    '!': Operator('!', 6, 1, factorial, input_after=False),

    # special implied operators. syntax: "< X >"
    '<!->': Operator("-", 10, 1, lambda num1: -num1, input_before=False),  # high priority sign minus
    '<;->': Operator("-", 2.5, 1, lambda num1: -num1, input_before=False)  # low priority sign minus
}
