from Operators import OPERATORS
from Analyzer import BRACKETS
"""
this module receives a list of tokens that are part of an expression,
converts it to a postfix expression and runs checks that the
expression is valid
"""

OPEN_BRACKET = "("
CLOSE_BRACKET = ")"


def convert_to_postfix(token_list: list) -> list:
    """
    converts a list of tokens to the corresponding prefix expression
    :param List[Union[int, str]] token_list: a list of numbers, operands and parenthesis that form an expression
    :return List[Union[int, str]]: returns the resulting postfix expression
    :raise SyntaxError: if given expression is with invalid
    :algorithm : this function uses an implementation of the "Shunting yard algorithm"
    """
    stack = []
    postfix = []

    for token in token_list:
        if isinstance(token, float):
            postfix.append(token)
        elif token in OPERATORS:
            while len(stack) > 0 and stack[-1] != OPEN_BRACKET and has_priority(stack[-1], token):
                postfix.append(stack.pop())
            stack.append(token)
        elif token == OPEN_BRACKET:
            stack.append(token)
        elif token == CLOSE_BRACKET:
            if OPEN_BRACKET not in stack:
                raise SyntaxError("invalid parenthesis order ")
            while stack[-1] != OPEN_BRACKET:
                postfix.append(stack.pop())
            stack.pop()  # pops '('

    if any(bracket in stack for bracket in set(*BRACKETS.items())):
        raise SyntaxError("invalid parenthesis order ")

    postfix.extend(reversed(stack))
    return postfix


def has_priority(operator1: str, operator2: str) -> bool:
    """
    returns if operator1 has priority over operator2
    :param str operator1: the first operator to check
    :param str operator2:  the second operator to check
    :return bool: returns if operator1 has_priority over operator2
    """
    if operator1 == operator2 and not OPERATORS[operator1].input_before and OPERATORS[operator1].inputs == 1:
        return False
    return OPERATORS[operator1].priority >= OPERATORS[operator2].priority
