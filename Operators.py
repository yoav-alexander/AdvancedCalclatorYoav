from Operations import divide, power, digit_sum, factorial


class Operator:
    """
    A basic class that represent an Operator

    :param str symbol: the symbol that represents the operator.
    :param float priority: the operator's priority in calculations
    :param int inputs: the number of input the operator receives
    :param Callable[..., float] function: a function that preforms the operators action
    :param bool input_before: boolean if the operator receives input before it (default: true)
    :param bool input_after: boolean if the operator receives input after it (default: true)
    """

    def __init__(self,
                 symbol: str,
                 priority: float,
                 inputs: int,
                 function,
                 input_before: bool = True,
                 input_after: bool = True,
                 inferred: bool = False):
        self.symbol = symbol
        self.priority = priority
        self.inputs = inputs
        self.function = function
        self.input_before = input_before
        self.input_after = input_after
        self.inferred = inferred


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

    # special implied operators.
    '<!->': Operator("-", 10, 1, lambda num1: -num1, input_before=False, inferred=True),
    '<;->': Operator("-", 3.5, 1, lambda num1: -num1, input_before=False, inferred=True)
}
