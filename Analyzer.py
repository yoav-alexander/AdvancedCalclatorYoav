from typing import List, Union


"""
this module receives an expression and splits it into
a list of tokens
"""

OPERATORS = "+-*/^@$&%~!"

def analyze_expression(expression: str) -> List[Union[int, str]]:
    """
    receives a string expression and converts it into a list basic tokens
    :param str expression: string expression
    :return  List[Union[int, str]: a list basic tokens
    :raise ValueError: if given invalid syntax
    """
    token_list = []
    num = ""
    for index, char in enumerate(expression):
        if part_of_number(expression, index):
            num += char
            continue

        if num != "":
            num = strip_minus(num)
            token_list.append(float(num.lstrip('.')))
            num = ""
        token_list.append(char)

    if num != "":
        num = strip_minus(num)
        token_list.append(float(num.lstrip('.')))

    return token_list


def strip_minus(num_str: str) -> str:
    """
    strips redundant '-' from given str
    :param str num_str: a string to strip
    :return: returns the strip after it was striped
    """
    if len(num_str) != 0 and num_str[0] == '-':
        return "-" + num_str.strip("-")
    return num_str


def part_of_number(expression: str, index: int) -> bool:
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
    return char not in OPERATORS or negative
