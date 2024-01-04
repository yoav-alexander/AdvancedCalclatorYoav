from typing import List
from Operators import OPERATORS, IMPLIED_OPERATORS

"""
this module receives an expression and splits it into
a list of tokens
"""

VALID_SYMBOLS = ''.join(filter(lambda op: op not in IMPLIED_OPERATORS, OPERATORS.keys())) + "()"
# all valid input symbols for the program
NUMERICS = ".0123456789"
VALID_INPUTS = VALID_SYMBOLS + NUMERICS

VALID_BEFORE = ")!"  # values apart from numbers that can be before an operator
VALID_AFTER = "S("  # values apart from numbers that can be after an operator


def analyze_expression(expression: str) -> List[float | str]:  # TODO add checks for 1+()+3
    """
    receives a string expression and converts it into a list basic tokens
    :param str expression: string expression
    :return  List[Union[float, str]]: a list basic tokens
    :raise ValueError: if given invalid number syntax or operator syntax
    """
    token_list = []
    num = ""
    for index, char in enumerate(expression):
        if char in NUMERICS:
            num += char
            continue

        if num != "":
            token_list.append(get_number(num))
            num = ""

        # checks for special operators
        for symbol, attributes in IMPLIED_OPERATORS.items():
            if attributes.check_func(expression, index):
                token_list.append(symbol)
                break
        else:
            token_list.append(char)

    if num != "":
        token_list.append(get_number(num))

    # checks if operators placements are possible
    is_valid_order(token_list)

    return token_list


def get_number(num_str: str) -> float:  # todo: add Doc Sting or remove
    # num_list = strip_minus(num_str)
    check_valid_number(num_str)  # checks if the number is in the correct syntax
    return float(num_str)


def check_valid_number(num: str) -> None:
    """
    check if the given number has valid syntax
    :param num: a string representing a number
    :raise ValueError: if the given number syntax is invalid
    """
    if num[0] == "." or num[-1] == ".":
        raise ValueError(f"invalid number syntax! '.' in invalid place: {num} ")
    try:
        float(num)
    except ValueError:
        raise ValueError(f"invalid number syntax: {num}")


def is_valid_order(token_list: List[float | str]) -> None:
    """
    checks if the operators placements are possible in the given operation
    :param  List[Union[float, str]] token_list: a list of token that form an expression
    :raise value error: if the operator placement is impossible
    """

    for index, token in enumerate(token_list):
        if token not in OPERATORS:
            continue

        if OPERATORS[token].input_before:
            if index == 0:
                raise ValueError(f" '{token}' operator can't be the at the start of an expression")
            if valid_symbol(token_list[index-1], VALID_BEFORE):
                error_message = f"{token_list[index - 1]} {token} {'X' if OPERATORS[token].input_after else ''}"
                raise ValueError(f"invalid syntax for operation: {error_message}")

        if OPERATORS[token].input_after:
            if index == len(token_list) - 1:
                raise ValueError(f" '{token}' operator can't be the at the end of an expression")
            if valid_symbol(token_list[index+1], VALID_AFTER):
                error_message = f"{'X' if OPERATORS[token].input_before else ''} {token} {token_list[index + 1]}"
                raise ValueError(f"invalid syntax for operation: {error_message}")


def valid_symbol(token: str | float, accepted_values: list[str] | str) -> bool:
    """
    returns if the given token is valid given the accepted_values given
    :param str | float token: a number or operator in the expression
    :param list[str] | str accepted_values: a list of accepted_values for the token
    :return bool: returns if the given token is valid given the accepted_values given
    """
    return isinstance(token, str) and token not in accepted_values

# def strip_minus(num_str: str) -> List[str | float]:
#     """
#     strips redundant '-' from the given str and splits to list
#     :param str num_str: a string to strip
#     :return List[str]: returns a list of a number and a minus sign if needed
#     """
#     num = num_str.strip("-")
#     return [num] if num_str.count('-') % 2 == 0 else ['s', num]


def is_valid_expression(expression: str) -> None:
    """
    returns if the given expression has invalid symbols in it
    :param string expression: an expression to check
    :raise ValueError: if the expression contains invalid symbols
    """

    for index, symbol in expression.split(" ")[:-1]:
        if symbol == expression[index+1]:
            raise ValueError(f"invalid spacing between number digits")

    expression = "".join(expression.split())

    for char in expression:
        if char not in VALID_INPUTS:
            raise ValueError(f"expression contains invalid symbol: {char}")
    if len(expression) == 0:
        raise ValueError("empty input")
