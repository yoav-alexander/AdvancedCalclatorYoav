from Operators import OPERATORS

"""
this module receives a postfix expression of operations and
calculates the final result
"""


def calculate_from_prefix(postfix_list: list) -> float:
    """
    return the solution to an expression in prefix notation
    :param List[Union[int, str]] postfix_list: a list of the expression in prefix notation
    :return float : returns the solution to the expression
    :raise SyntaxError: if the expression is unsolvable or invalid
    """
    changed = False  # marks if the list was changed during the iteration
    index = -1
    while len(postfix_list) > 1:
        index += 1

        if all(isinstance(token, float) for token in postfix_list):
            raise SyntaxError("expression invalid! are you missing any operators? ")
        if index == len(postfix_list):
            if not changed:
                faulty_operators = " or ".join([token for token in postfix_list if token in OPERATORS])
                raise SyntaxError(f"expression invalid! there is something wrong near {faulty_operators}")
            changed = False
        index = index % len(postfix_list)
        token = postfix_list[index]

        if isinstance(token, float):
            continue

        # print("\t", index, "list:", postfix_list)
        args = postfix_list[index - OPERATORS[token].inputs: index]
        if not is_valid_args(args) or len(args) != OPERATORS[token].inputs:
            continue

        # print("\t", token, "args: ", args)
        try:
            result = OPERATORS[token].function(*args)
        except ArithmeticError as e:
            raise SyntaxError(e)
        del postfix_list[index - OPERATORS[token].inputs: index + 1]  # removes the operation from the list
        postfix_list.insert(index - OPERATORS[token].inputs, result)  # inserts the operation's result to the list
        changed = True

    # print("\t", index, "list:", postfix_list)
    return postfix_list[0] if postfix_list[0] % 1 != 0 else int(postfix_list[0])


def is_valid_args(args: list[float]) -> bool:
    """
    returns if the list of args is valid function inputs
    :param  list[float] args: a list of args to check
    :return bool: returns if the list of args is valid function inputs
    """
    return all(isinstance(arg, float) for arg in args)
