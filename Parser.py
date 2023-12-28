from typing import List, Union
from Operators import OPERATORS

"""
this module receives a list of tokens that are part of an expression,
converts it to a postfix expression and runs checks that the
expression is valid
"""


def convert_to_postfix(token_list: List[Union[int, str]]) -> List[Union[int, str]]:
    """
    converts a list of tokens to the corresponding prefix expression
    :param List[Union[int, str]] token_list: a list of numbers, operands and parenthesis that form an expression
    :return List[Union[int, str]]: returns the resulting postfix expression
    """
    # :algorithm : this function uses an implementation the Shunting yard algorithm
    stack = []
    postfix = []

    for token in token_list:
        if isinstance(token, float):
            postfix.append(token)
        elif token in OPERATORS:
            while len(stack) > 0 and stack[-1] != '(' and has_priority(stack[-1], token):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()  # pops '('
    postfix.extend(reversed(stack))
    return postfix


def has_priority(operator1: str, operator2: str) -> bool:
    """
    returns if operator1 has_priority over operator2
    :param str operator1: the first operator to check
    :param str operator2:  the second operator to check
    :return bool: returns if operator1 has_priority over operator2
    """
    return OPERATORS[operator1].priority >= OPERATORS[operator2].priority
