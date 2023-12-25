from Analyzer import analyze_expression

VALID_INPUTS = ['+', '-', '*', '/', '^', '@', '$', '&', '%', '~', '!', '.']


def get_expression() -> str:
    """
    receives from the user an expression to evaluate
    :return str: the given expression
    """
    try:
        expression = input("Enter an expression for the calculator:\n\t")
    except EOFError:
        return "invalidInput"
    return expression.strip(" ")


def is_valid_expression(expression: str) -> bool:
    return all(char in VALID_INPUTS or char.isnumeric() for char in expression)


def main():

    expression = get_expression()
    if expression == "invalidInput":
        print(expression)
        return

    if not is_valid_expression(expression):
        print("expression contains invalid inputs")
        return

    # analyze (Analyzer.py)
    token_ls = analyze_expression(expression)

    # parse to tree (Parser.py)

    # get solution from tree (CalculateOperations.py)


if __name__ == '__main__':
    main()
