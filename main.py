import ply.lex as lex
import ply.yacc as yacc

import cool_programs


bool_const = "BOOL_CONST"

bool_const_values = {
    "true": True,
    "false": False
}


def value_lookup(token_value):
    try:
        return bool_const_values[token_value]
    except KeyError:
        return token_value


reserved_words = {
    "class": "CLASS",
    "else": "ELSE",
    "true": bool_const,
    "false": bool_const,
    "fi": "FI",
    "if": "IF",
    "in": "IN",
    "inherits": "INHERITS",
    "isvoid": "ISVOID",
    "let": "LET",
    "loop": "LOOP",
    "pool": "POOL",
    "then": "THEN",
    "while": "WHILE",
    "case": "CASE",
    "esac": "ESAC",
    "new": "NEW",
    "of": "OF",
    "not": "NOT",
}


symbol_mapping = {
    ":": "COLON",
    "{": "LBRACK",
    "}": "RBRACK",
    "(": "LPAR",
    ")": "RPAR",
    "-": "MINUS",
    "*": "TIMES",
    "/": "DIVIDE"
}

# List of token names

tokens = (
    "ASSIGNMENT",
    "PLUS",
    "COMMA",
    "SEMICOLON",
    "IDENTIFIER",
    "TYPE",
    "INTEGER",
    "STR_CONST",
    "SYMBOL",
    "NEWLINE",
    "whitespace",
)

tokens = tokens + tuple(reserved_words.values()) + tuple(symbol_mapping.values())
tokens = tuple(set(tokens))

t_ASSIGNMENT = "<-"

t_PLUS = "\+"

t_COMMA = ","
t_SEMICOLON = ";"


def t_SYMBOL(t):
    "[:{}\(\)\-\*\/]"
    t.type = symbol_mapping[t.value]
    return t


def t_whitespace(t):
    "[ \n\f\r\t\v]"


def t_TYPE(t):
    r"[A-Z][_a-zA-Z0-9]{0,30}"
    return t


def t_IDENTIFIER(t):
    r"[_a-zA-Z][_a-zA-Z0-9]{0,30}"
    t.type = reserved_words.get(t.value, "IDENTIFIER")
    t.value = value_lookup(t.value)
    return t



def t_INTEGER(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


def t_STR_CONST(t):
    r'".*"'
    t.value = t.value.replace('"', '')
    return t


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    t.lexer.skip(1)
    return t


# SYNTAX


def p_program(p):
    """
    program : class_list
    """
    p[0] = ("COOL program", p[1])


def p_empty(p):
    """
    empty :
    """
    pass


def p_class_list(p):
    """
    class_list : class class_list
    class_list : empty
    """
    if len(p) > 2:
        p[0] = tuple(["LIST-OF-CLASSES"] + p[1:])
    else:
        p[0] = ("EMPTY-CLASS-LIST",)


def p_class(p):
    """
    class : CLASS TYPE LBRACK feature_list RBRACK
    class : CLASS TYPE INHERITS TYPE LBRACK feature_list RBRACK
    """
    p[0] = tuple(["CLASS-DECLARATION"] + p[1:])


def p_feature_list(p):
    """
    feature_list : feature feature_list
    feature_list : empty
    """
    if len(p) > 2:
        p[0] = tuple(["LIST-OF-FEATURES"] + p[1:])
    else:
        p[0] = ("EMPTY-FEATURE-LIST",)


def p_feature(p):
    """
    feature : exp SEMICOLON
    feature : IDENTIFIER COLON TYPE SEMICOLON
    feature : IDENTIFIER COLON TYPE ASSIGNMENT exp SEMICOLON
    feature : IDENTIFIER LPAR RPAR COLON TYPE LBRACK exp RBRACK SEMICOLON
    """
    # TODO remove expression from class body

    p[0] = tuple(["FEATURE"] + p[1:])


# def p_formal_list(p):
#     """
#     formal_list : formal formal_list
#     formal_list : empty
#     """
#     if len(p) > 2:
#         p[0] = tuple(["LIST-OF-FORMALS"] + p[1:])
#     else:
#         p[0] = ("EMPTY-FORMAL-LIST",)
#
#
# def p_formal(p):
#     """
#     formal : IDENTIFIER ':' TYPE SEMICOLON
#     """
#     p[0] = tuple(("ATTRIBUTE DECLARATION", ) + p[1:])


def p_exp(p):
    """
    exp : exp PLUS exp
    """
    p[0] = ("SUM-EXPRESSION", p[2], p[1], p[3])


def p_integer(p):
    """
    exp : INTEGER
    """
    p[0] = ("EXPRESSION-TO-INTEGER", p[1])


if __name__ == "__main__":
    from pprint import pprint
    lexer = lex.lex()
    parser = yacc.yacc()

    desc, tree = parser.parse(input=cool_programs.current_developing, lexer=lexer)

    input("\nType anything to continue")

    print(f"------- {desc} ---------\n")
    pprint(tree)
    print("----------\n")

    results = [(desc, parser.parse(input=test_data, lexer=lexer)) for desc, test_data in cool_programs.test_programs.items()]

    input("Type anything to continue")

    for result in results:
        desc, tree = result
        print(f"------- {desc} ---------\n")
        pprint(tree)
        print("----------\n")
