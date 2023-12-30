from typing import List, Union
from Operators import OPERATORS

"""
this module receives an expression and splits it into
a list of tokens
"""

VALID_SYMBOLS = ''.join(OPERATORS.keys()) + "()"
# all valid input symbols for the program
VALID_INPUTS = VALID_SYMBOLS + ".0123456789"


def analyze_expression(expression: str) -> List[Union[int, str]]:
    """
    receives a string expression and converts it into a list basic tokens
    :param str expression: string expression
    :return  List[Union[int, str]: a list basic tokens
    :raise ValueError: if given invalid number syntax or operator syntax
    """
    token_list = []
    num = ""
    for index, char in enumerate(expression):
        if is_part_of_number(expression, index):
            num += char
            continue

        if num != "":
            num = strip_minus(num)
            try:
                token_list.append(float(num.lstrip('.')))
            except ValueError:
                raise ValueError(f"invalid number syntax: {num}")
            num = ""

        token_list.append(char)

    if num != "":
        num = strip_minus(num)
        token_list.append(float(num.lstrip('.')))

    # checks if operators placements are possible
    is_valid_order(token_list)

    return token_list


def is_valid_order(token_list: List[Union[int, str]]):
    """
    checks if the operators placements are possible in the given operation
    :param  List[Union[int, str]] token_list: a list of token that form an expression
    :raise value error: if the operator placement is impossible
    """

    for index, token in enumerate(token_list):
        if token not in OPERATORS:
            continue

        if OPERATORS[token].input_before:
            if index == 0:
                raise ValueError(f" '{token}' operator can't be the at the start of an expression")
            if isinstance(token_list[index - 1], str) and token_list[index - 1] != ")":
                raise ValueError(f"invalid syntax for operation: {token_list[index - 1]} {token} X")

        if OPERATORS[token].input_after:
            if index == len(token_list) - 1:
                raise ValueError(f" '{token}' operator can't be the at the end of an expression")
            if isinstance(token_list[index + 1], str) and token_list[index + 1] != "(":
                raise ValueError(f"invalid syntax for operation: X {token} {token_list[index + 1]}")


def strip_minus(num_str: str) -> str:
    """
    strips redundant '-' from the given str
    :param str num_str: a string to strip
    :return: returns the strip after it was striped
    """
    return num_str.strip("-") if num_str.count('-') % 2 == 0 else '-' + num_str.strip("-")


def is_part_of_number(expression: str, index: int) -> bool:
    """
    returns if a char in place "index" is a part of a number
    :param string expression: the whole expression
    :param int index: index to check
    :return: returns if a char in place "index" is a part of a number
    """
    char = expression[index]
    before_numeric = index != 0 and expression[index - 1].isnumeric()
    after_numeric = index < len(expression) - 1 and expression[index + 1] in "0123456789-"
    negative = char == '-' and not before_numeric and after_numeric
    return char not in VALID_SYMBOLS or negative


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
