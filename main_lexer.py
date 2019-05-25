import ply.lex as lex
from utils import tokenize

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

t_ASSIGNMENT = "="

t_PLUS = "\+"

t_COMMA = ","
t_SEMICOLON = ";"


def t_SYMBOL(t):
    r"[:{}\(\)\-\*\/]"
    t.type = symbol_mapping[t.value]
    return t


def t_whitespace(t):
    r"[ \n\f\r\t\v]"


def t_IDENTIFIER(t):
    r"[_a-zA-Z][_a-zA-Z0-9]{0,30}"
    t.type = reserved_words.get(t.value, "IDENTIFIER")
    t.value = value_lookup(t.value)
    return t


def t_TYPE(t):
    r"[A-Z][_a-zA-Z0-9]{0,30}"
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


lexer = lex.lex()

data = cool_programs.program_5

tokens = tokenize(lexer, data)

print(tokens)

# for token in tokens:
#     print(token)
#     input()



