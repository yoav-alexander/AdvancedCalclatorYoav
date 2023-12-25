from Analyzer import analyze_expression, OPERATORS

VALID_INPUTS = OPERATORS + ".0123456789"


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


def main():

    try:
        expression = get_expression()
    except EOFError:
        print("invalidInput")
        return

    if not is_valid_expression(expression):
        print("expression contains invalid inputs")
        return

    # analyze (Analyzer.py)
    try:
        token_ls = analyze_expression(expression)
    except ValueError as ve:
        print(ve)
        return
    print(token_ls)
    # parse to tree (Parser.py)

    # get solution from tree (CalculateOperations.py)


if __name__ == '__main__':
    main()
