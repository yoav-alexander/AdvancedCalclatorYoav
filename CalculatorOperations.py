from functools import lru_cache
from typing import List, Union

from Analyzer import OPERATORS
from Operations import *
"""
this module receives a tree of operations and
calculates the final result
"""


def factorial(num1: int) -> int:
    # check if whole number and positive
    if num1 in [0, 1]:
        return 1
    return num1 * factorial(num1 - 1)


CALCULATIONS = {'+': lambda num1, num2: num1 + num2,
                '-': lambda num1, num2: num1 - num2,
                '*': lambda num1, num2: num1 * num2,
                '/': lambda num1, num2: num1 / num2,
                '^': lambda num1, num2: num1 ** num2,
                '@': lambda num1, num2: (num1 + num2) / 2,
                '$': lambda num1, num2: max(num1, num2),
                '&': lambda num1, num2: min(num1, num2),
                '%': lambda num1, num2: num1 % num2,
                '~': lambda num: -num,
                '!': factorial}
INPUTS = {'+': 2, '-': 2, '*': 2, '/': 2, '^': 2, '@': 2, '$': 2, '&': 2, '%': 2, '~': 1, '!': 1}


def calculate_from_prefix(postfix_list: List[Union[int, str]]) -> float:
    """
    return the solution to an expression in prefix notation
    :param List[Union[int, str]] postfix_list: a list of the expression in prefix notation
    :return float : returns the solution to the expression
    """

    index = 0
    while len(postfix_list) > 1:
        # print(index, "list:", postfix_list)
        index = index % len(postfix_list)
        token = postfix_list[index]

        if isinstance(token, str):
            args = postfix_list[index - INPUTS[token]: index]
            if not is_valid_args(args):
                index += 1
                continue
            # print("args: ", args)
            result = CALCULATIONS[token](*args)
            del postfix_list[index - INPUTS[token]: index + 1]
            postfix_list.insert(index - INPUTS[token], result)
        index += 1
    return postfix_list[0]


def is_valid_args(args: list[float]) -> bool:
    """
    returns if the list of args is valid function inputs
    :param  list[float] args: a list of args to check
    :return bool: returns if the list of args is valid function inputs
    """
    return all(isinstance(arg, float) for arg in args)
