from typing import List, Union
from Analyzer import VALID_SYMBOLS, OPERATORS

"""
this module receives a list of tokens that are part of an expression,
converts it to a postfix expression and runs checks that the
expression is valid
"""

PRIORITIES = {'+': 1, '-': 2, '*': 2, '/': 2, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6}


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
            while len(stack) > 0 and stack[-1] != '(' and PRIORITIES[stack[-1]] >= PRIORITIES[token]:
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
