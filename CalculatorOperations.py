from typing import List, Union
from Operators import OPERATORS

"""
this module receives a tree of operations and
calculates the final result
"""


def calculate_from_prefix(postfix_list: List[Union[int, str]]) -> float:
    """
    return the solution to an expression in prefix notation
    :param List[Union[int, str]] postfix_list: a list of the expression in prefix notation
    :return float : returns the solution to the expression
    :raise ValueError: if the expression is unsolvable or invalid
    """
    changed = True  # marks if the list was changed during the iteration
    index = -1
    while len(postfix_list) > 1:
        if index == len(postfix_list) and not changed:
            raise ValueError("the given expression is invalid")
        changed = True

        index += 1
        print(index, "list:", postfix_list)
        index = index % len(postfix_list)
        token = postfix_list[index]

        if isinstance(token, float):
            changed = False
            continue
        args = postfix_list[index - OPERATORS[token].inputs: index]
        if not is_valid_args(args):
            changed = False
            continue
        print("args: ", args)
        result = OPERATORS[token].function(*args)
        del postfix_list[index - OPERATORS[token].inputs: index + 1]  # removes the operation from the list
        postfix_list.insert(index - OPERATORS[token].inputs, result)  # inserts the operation's result to the list
    return postfix_list[0]


def is_valid_args(args: list[float]) -> bool:
    """
    returns if the list of args is valid function inputs
    :param  list[float] args: a list of args to check
    :return bool: returns if the list of args is valid function inputs
    """
    return all(isinstance(arg, float) for arg in args)
