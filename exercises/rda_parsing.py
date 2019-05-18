"""
Recursive Descent Algorithm
"""

# Grammar

"""
E -> E_x + id | E_x
E_x -> |id * E_x| id | ( E )
"""

next_token = -1

char_string = ["id", "*", "(", "id", "+", "id", ")"]


def term(token):
    global char_string, next_token
    try:
        next_token += 1
        return_value = char_string[next_token] == token
        return return_value
    except IndexError:
        return True


def derivation_E1():
    """
    E_x + id
    """
    return non_terminal_E_x() and term("+") and term("id")


def derivation_E2():
    """
    E_x
    """
    return non_terminal_E_x()


def non_terminal_start_E():
    """
    E -> E_x + id | E_x
    """
    global next_token

    save = int(next_token)
    for derivation in (derivation_E1, derivation_E1):
        next_token = int(save)
        if derivation():
            return True

    return False


def derivation_E_x_1():
    """
    id * E_x
    """
    return term("id") and term("*") and non_terminal_E_x()


def derivation_E_x_2():
    """
    id
    """
    return term("id")


def derivation_E_x_3():
    """
    (E)
    """
    return term("(") and non_terminal_start_E() and term(")")


def non_terminal_E_x():
    """
    E_x -> |id * E_x| id | ( E )
    """
    global next_token

    save = int(next_token)

    for derivation in (derivation_E_x_1, derivation_E_x_2, derivation_E_x_3):
        next_token = int(save)
        if derivation():
            return True
    return False


if __name__ == "__main__":
    print(non_terminal_start_E())

