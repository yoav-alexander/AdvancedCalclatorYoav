from Operations import divide, power, digit_sum, factorial
from Operators import Operator, Implied_operators, is_sign_minus


class ExpressionSyntaxError(Exception):
    """Exception raised for any error in expression syntax

        Attributes:
            message -- explanation of the error
        """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


OPERATORS = {
    '+': Operator(1, 2, lambda num1, num2: num1 + num2),
    '-': Operator(1, 2, lambda num1, num2: num1 - num2),
    '*': Operator(2, 2, lambda num1, num2: num1 * num2),
    '/': Operator(2, 2, divide),
    '^': Operator(3, 2, power),

    '%': Operator(4, 2, lambda num1, num2: num1 % num2),
    '@': Operator(5, 2, lambda num1, num2: (num1 + num2) / 2),
    '$': Operator(5, 2, lambda num1, num2: max(num1, num2)),
    '&': Operator(5, 2, lambda num1, num2: min(num1, num2)),
    '~': Operator(6, 1, lambda num1: -num1, input_before=False),
    '#': Operator(6, 1, digit_sum, input_after=False),
    '!': Operator(6, 1, factorial, input_after=False),
}

IMPLIED_OPERATORS = {
    'S': Implied_operators(10, 1, lambda num1: -num1, is_sign_minus, input_before=False)
}
OPERATORS.update(IMPLIED_OPERATORS)

NON_COLLECTING_OPERATORS = "#$@&!^"  # a list of operators which do their operation before updating the number sign



