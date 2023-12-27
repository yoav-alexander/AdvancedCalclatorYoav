from Analyzer import analyze_expression, VALID_SYMBOLS
from Parser import convert_to_postfix

VALID_INPUTS = VALID_SYMBOLS + ".0123456789"


def get_expression() -> str:
    """
    receives from the user an expression to evaluate
    :return str: the given expression
    :raise EOFError: if given in valid input
    """
    expression = input("Enter an expression for the calculator:\n\t")
    return expression.strip(" ")


def is_valid_expression(expression: str) -> bool:
    """
    returns if the given expression has invalid symbols in it
    :param string expression: an expression to check
    :return: returns if the given expression has invalid symbols in it
    """
    return all(char in VALID_INPUTS for char in expression)


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    """
    if not is_valid_expression(expression):
        raise ValueError

    # analyze (Analyzer.py)
    token_ls = analyze_expression(expression)
    print(token_ls)
    # parse to tree (Parser.py)
    post_fix = convert_to_postfix(token_ls)
    print(post_fix)

    # get solution from tree (CalculateOperations.py)


def main():
    expression = get_expression()
    calculate_expression(expression)


if __name__ == '__main__':
    main()
