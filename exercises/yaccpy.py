import ply.lex as lex
import ply.yacc as yacc

from utils import tokenize

# LEXER

symbol_mapping = {
    "+": "PLUS",
    "-": "MINUS",
    "*": "TIMES",
    "/": "DIVIDE",
    "(": "LPAR",
    ")": "RPAR"
}


# TOKENS DEFINITIONS

tokens = (
    "LPAR",
    "RPAR",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "DIGIT",
    "SYMBOL",
    "whitespace"
)


def t_whitespace(t):
    "[ \n\f\r\t\v]"


def t_SYMBOL(t):
    "[+\-\*\/\(\)]"
    t.type = symbol_mapping[t.value]
    return t


def t_DIGIT(t):
    "[0-9]+"
    t.value = int(t.value)
    return t


def t_error(t):
    t.lexer.skip(1)
    return t

# PARSER

# GRAMMAR DEFINITION


"""
exp -> exp + exp
exp -> exp - exp
exp -> exp * exp
exp -> exp / exp
exp -> ( exp )
exp -> DIGIT
"""

expression_name_mapping = {
    "+": "sum-expression",
    "-": "sub-expression",
    "*": "multi-expression",
    "/": "division-expression"
}


def p_exp_op(p):
    """exp : exp PLUS exp
           | exp MINUS exp
           | exp TIMES exp
           | exp DIVIDE exp
    """

    p[0] = (expression_name_mapping[p[2]], p[2], p[1], p[3])


def p_exp_digit(p):
    "exp : DIGIT"
    p[0] = ("number-expression", p[1])


def p_par_exp(p):
    "exp : LPAR exp RPAR"
    p[0] = ("parenthesis-expression", p[1], p[2], p[3])


if __name__ == "__main__":
    input_string = input("Enter an arithmetic expression >")
    lexer = lex.lex()
    parser = yacc.yacc()
    result = parser.parse(input=input_string, lexer=lexer)
    print(result)
