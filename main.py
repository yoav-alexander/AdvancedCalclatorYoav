from Analyzer import analyze_expression, is_valid_expression
from OperationsCalculator import calculate_from_prefix
from Parser import convert_to_postfix


def get_expression() -> str:
    """
    receives from the user an expression to evaluate
    :return str: the given expression
    :raise EOFError: if given in valid input
    """
    expression = input("Enter an expression for the calculator:\n\t")
    return expression.replace(" ", "")


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    """
    is_valid_expression(expression)
    token_ls = analyze_expression(expression)  # splits the expression to tokens
    print(token_ls)
    post_fix = convert_to_postfix(token_ls)  # convert the expression to postfix
    print(post_fix)
    result = calculate_from_prefix(post_fix)  # gets the final result from postfix expression
    return result


def main():
    expression = get_expression()
    print(expression)
    print("result:", calculate_expression(expression))


if __name__ == '__main__':
    main()
