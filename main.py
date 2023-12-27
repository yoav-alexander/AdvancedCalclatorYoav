from Analyzer import analyze_expression, VALID_SYMBOLS
from CalculatorOperations import calculate_from_prefix
from Parser import convert_to_postfix

# Operator = namedtuple('Operator', "symbol priority inputs function ")
# OPERATORS = [
#     Operator('+', 1, 2),
#     Operator('+', 1, 2),
#     Operator('+', 1, 2),
#     Operator('+', 1, 2),
#     Operator('+', 1, 2),
#     Operator('+', 1, 2),
#
# ]

# all valid input symbols for the program
VALID_INPUTS = VALID_SYMBOLS + ".0123456789"


def get_expression() -> str:
    """
    receives from the user an expression to evaluate
    :return str: the given expression
    :raise EOFError: if given in valid input
    """
    expression = input("Enter an expression for the calculator:\n\t")
    return expression.replace(" ", "")


def is_valid_expression(expression: str):
    """
    returns if the given expression has invalid symbols in it
    :param string expression: an expression to check
    :raise ValueError: if the expression contains invalid symbols
    """
    for char in expression:
        if char not in VALID_INPUTS:
            raise ValueError(f"expression contains invalid symbol: {char}")
    if len(expression) == 0:
        raise ValueError("empty input")


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    """
    is_valid_expression(expression)
    # analyze
    token_ls = analyze_expression(expression)
    print(token_ls)
    # parse to postfix
    post_fix = convert_to_postfix(token_ls)
    print(post_fix)
    # get solution from postfix
    result = calculate_from_prefix(post_fix)
    return result


def main():
    expression = get_expression()
    print(expression)
    print(calculate_expression(expression))


if __name__ == '__main__':
    main()
