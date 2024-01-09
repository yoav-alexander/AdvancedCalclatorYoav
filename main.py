from Analyzer import analyze_expression, is_valid_expression
from Operations_calculator import calculate_from_prefix
from Parser import convert_to_postfix
from config import ExpressionSyntaxError


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    :raise ExpressionSyntaxError: if the given expression is invalid
    """
    is_valid_expression(expression)
    expression = "".join(expression.split())
    token_ls = analyze_expression(expression)  # splits the expression to tokens
    print(f"Token list: {token_ls}")
    post_fix = convert_to_postfix(token_ls)  # convert the expression to postfix
    print(f"Post fix: {post_fix}")
    result = calculate_from_prefix(post_fix)  # gets the final result from postfix expression
    return result


def main():

    try:
        expression = input("Enter an expression for the calculator:\n\t")
    except EOFError:
        print("invalid input")
        return

    try:
        result = calculate_expression(expression)
    except ExpressionSyntaxError as e:
        print(e)
        return

    print(f"{expression} = {result} ")


if __name__ == '__main__':
    main()
