from Operators import OPERATORS

"""
this module receives an expression and splits it into
a list of tokens
"""

VALID_SYMBOLS = ''.join(filter(lambda op: op[0] != '<' and op[-1] != '>', OPERATORS)) + "()"
# all valid input symbols for the program
NUMERICS = ".0123456789"
VALID_INPUTS = VALID_SYMBOLS + NUMERICS

# values apart from numbers that can be before an operator
VALID_BEFORE = ")" + ''.join(op for op in OPERATORS if not OPERATORS[op].input_after)
# values apart from numbers that can be after an operator
VALID_AFTER = "(" + ''.join(op for op in OPERATORS if not OPERATORS[op].input_before)


def analyze_expression(expression: str) -> list:
    """
    receives a string expression and converts it into a list basic tokens
    :param str expression: string expression
    :return  List[Union[float, str]]: a list basic tokens
    :raise SyntaxError: if given invalid number syntax or operator syntax
    """
    token_list = []
    num = ""
    for index, char in enumerate(expression):
        if char in NUMERICS:
            num += char
            continue

        if num != "":
            check_valid_number(num)  # checks if the number is in the correct syntax
            token_list.append(float(num))  # it's ok to cast because "check_valid_number"
            num = ""

        token_list.append(char)

    if num != "":
        check_valid_number(num)  # checks if the number is in the correct syntax
        token_list.append(float(num))  # it's ok to cast because "check_valid_number"

    token_list = convert_sign_minus(token_list)

    print(token_list)
    # checks if operators placements are possible
    is_valid_order(token_list)

    return token_list


def convert_sign_minus(token_list: list) -> list:
    """
    returns the given token list but with all the sign minus replaced with their corresponding symbols
    :param List[float | str] token_list: a list basic tokens repressing an expression
    :return  List[float | str]: returns the given token list but with all the sign minus
    replaced with their corresponding symbols
    """
    for index, token in enumerate(token_list):  # 5! -- 3
        if is_sign_minus(token_list, index):
            if index == 0 or token_list[index-1] in ["(", "<;->"]:
                token_list[index] = "<;->"  # low priority sign minus
            elif token_list[index - 1] in OPERATORS:  # OPERATORS includes <!-> ( <;-> caught earlier)
                token_list[index] = "<!->"  # high priority sign minus
    return token_list


def is_sign_minus(token_list: list, index: int) -> bool:
    """
    returns if the given expression is a sign minus
    :param List[float | str] token_list: a list basic tokens repressing an expression
    :param int index: the index of the suspected sign minus
    :return bool: returns if the given expression is a sign minus
    """
    valid_previse_symbols = [op for op in OPERATORS if OPERATORS[op].input_after] + ["("]

    valid_before = index == 0 or token_list[index - 1] in valid_previse_symbols
    valid_after = (index == len(token_list) - 1
                   or isinstance(token_list[index + 1], float)
                   or token_list[index + 1] in ["(", "-"])
    return token_list[index] == "-" and valid_before and valid_after


def check_valid_number(num: str) -> None:
    """
    check if the given number has valid syntax
    :param str num: a string representing a number
    :raise SyntaxError: if the given number syntax is invalid
    """
    if num[0] == "." or num[-1] == ".":
        raise SyntaxError(f"invalid number syntax! '.' in invalid place: {num} ")
    try:
        float(num)
    except ValueError:
        raise SyntaxError(f"invalid number syntax: {num}")


def is_valid_order(token_list: list) -> None:
    """
    checks if the operators placements are possible in the given operation
    :param  List[float | str] token_list: a list of token that form an expression
    :raise SyntaxError: if the operator placement is impossible
    """

    for index, token in enumerate(token_list):

        if token == "(" and index < len(token_list) - 1 and token_list[index + 1] == ")":
            raise SyntaxError("invalid parenthesis syntax '()' ")

        if token not in OPERATORS:
            continue

        if OPERATORS[token].input_before:
            if index == 0:
                raise SyntaxError(f" '{token}' operator can't be the at the start of an expression")
            if valid_symbol(token_list[index-1], VALID_BEFORE):
                error_message = f"{token_list[index - 1]} {token} {'X' if OPERATORS[token].input_after else ''}"
                raise SyntaxError(f"invalid syntax for operation: {error_message}")

        if OPERATORS[token].input_after:
            if index == len(token_list) - 1:
                raise SyntaxError(f" '{token}' operator can't be the at the end of an expression")
            if valid_symbol(token_list[index+1], VALID_AFTER):
                error_message = f"{'X' if OPERATORS[token].input_before else ''} {token} {token_list[index + 1]}"
                raise SyntaxError(f"invalid syntax for operation: {error_message}")

        if token == "~" and token_list[index+1] == "~":
            raise SyntaxError(f"invalid syntax for operation: ~~ ")


def valid_symbol(token: str | float, accepted_values: list[str] | str) -> bool:
    """
    returns if the given token is valid given the accepted_values given
    :param str | float token: a number or operator in the expression
    :param list[str] | str accepted_values: a list of accepted_values for the token
    :return bool: returns if the given token is valid given the accepted_values given
    """
    return isinstance(token, str) and token not in accepted_values


def is_valid_expression(expression: str) -> None:
    """
    returns if the given expression has invalid symbols in it
    :param string expression: an expression to check
    :raise SyntaxError: if the expression contains invalid symbols
    """

    # for index, symbol in enumerate(expression.split(" ")[:-1]):
    #     print(index, symbol)
    #     if symbol in NUMERICS and expression[index+1] in NUMERICS:
    #         raise SyntaxError(f"invalid spacing between number digits")

    expression = "".join(expression.split())
    for char in expression:
        if char not in VALID_INPUTS:
            raise SyntaxError(f"expression contains invalid symbol: {char}")
    if len(expression) == 0:
        raise SyntaxError("empty input")
