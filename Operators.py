from typing import Callable
from Operations import divide, power, factorial


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
                 priority: float,
                 inputs: int,
                 function: Callable[..., float],
                 input_before: bool = True,
                 input_after: bool = True):
        self.priority = priority
        self.inputs = inputs
        self.function = function
        self.input_before = input_before
        self.input_after = input_after


class Implied_operators(Operator):
    """
    A class that represent an Operator that is not in the expression,
    but it can be implied by it

    Attributes:
        priority: float
        inputs: int
        function: Callable[..., float]
        input_before: bool = True
        input_after: bool = True
    """
    def __init__(self, priority: float, inputs: int, function: Callable[..., float],
                 check_func: Callable[[str, int], bool], input_before: bool = True, input_after: bool = True):
        super().__init__(priority, inputs, function, input_before, input_after)
        self.check_func = check_func


OPERATORS = {
    '+': Operator(1, 2, lambda num1, num2: num1 + num2),
    '-': Operator(1, 2, lambda num1, num2: num1 - num2),
    '*': Operator(2, 2, lambda num1, num2: num1 * num2),
    '/': Operator(2, 2, divide),
    '^': Operator(3, 2, power),
    '@': Operator(5, 2, lambda num1, num2: (num1 + num2) / 2),
    '$': Operator(5, 2, lambda num1, num2: max(num1, num2)),
    '&': Operator(5, 2, lambda num1, num2: min(num1, num2)),
    '%': Operator(4, 2, lambda num1, num2: num1 % num2),
    '~': Operator(6, 1, lambda num1: -num1, input_before=False),
    '!': Operator(6, 1, factorial, input_after=False)
}

IMPLIED_OPERATORS = {
    'S': Implied_operators(10, 1, lambda num1: -num1, is_sign_minus, input_before=False)
}
OPERATORS.update(IMPLIED_OPERATORS)


