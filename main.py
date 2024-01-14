from Analyzer import analyze_expression, is_valid_expression
from Expression_calculator import calculate_from_prefix
from Parser import convert_to_postfix


def calculate_expression(expression: str) -> float:
    """
    receives and expression and returns its result
    :param str expression: an expression to be evaluated
    :return float : returns the solution to the given expression
    :raise SyntaxError: if the given expression is invalid
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

    # try:
    #     expression = input("Enter an expression for the calculator:\n\t")
    # except EOFError:
    #     print("invalid input")
    #     return
    #
    # try:
    #     result = calculate_expression(expression)
    # except SyntaxError as e:
    #     print(e)
    #     return
    #
    # print(f"{expression} = {result} ")

    print("1. -1+7 = 6,", calculate_expression("-1+7"))
    print("2. -2^3 = -8,", calculate_expression("-2^3"))
    print("2.1. (-3^2+4) = -5,", calculate_expression("(-3^2+4)"))
    print("3. -3 ^ 2 = -9,", calculate_expression("-3 ^ 2 "))
    print("4. 3+~-3 = 6,", calculate_expression("3+~-3"))
    print("5. ~-3!= 6,", calculate_expression("~-3!"))
    try:
        print("6!. ~--3! = X,")
        calculate_expression("~--3!")  # -> ~(--3)!
    except Exception as e:
        print("\t", e)
    try:
        print("7. --~--3 = X,")
        calculate_expression("--~--3")
    except Exception as e:
        print("\t", e)
    try:
        print("8!. ~~3 = X,")
        calculate_expression("~~3")
    except Exception as e:
        print("\t", e)
    try:
        print("9. 2 - - 3! = X,")
        calculate_expression("2 - - 3!")
    except Exception as e:
        print("\t", e)
    print("10. -3! = -6,", calculate_expression("-3!"))
    print("11. --3! = 6,", calculate_expression("--3!"))  # ->
    print("12. 2---3! = -4,", calculate_expression("2---3!"))
    print("13. 2+--3! = 8,", calculate_expression("2+--3!"))


if __name__ == '__main__':
    main()
