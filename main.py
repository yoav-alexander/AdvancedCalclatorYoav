from Analyzer import analyze_expression, is_valid_expression
from Expression_calculator import calculate_from_prefix
from Parser import convert_to_postfix


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    :raise SyntaxError: if the given expression is invalid
    :raise ArithmeticError: if attempted to do an invalid operation
    """
    is_valid_expression(expression)
    expression = "".join(expression.split())

    token_ls = analyze_expression(expression)  # splits the expression to tokens
    # print(f"{token_ls=}")
    post_fix = convert_to_postfix(token_ls)  # convert the expression to postfix
    # print(f"{post_fix=}")
    result = calculate_from_prefix(post_fix)  # gets the final result from postfix expression
    return round(result, 10)


def main():

    try:
        expression = input("Enter an expression for the calculator:\n\t")
    except EOFError:
        print("invalid input")
        return

    try:
        result = calculate_expression(expression)
    except (SyntaxError, ArithmeticError) as e:
        print(e)
        return

    print(f"{expression} = {result:g} ")


if __name__ == '__main__':
    main()
