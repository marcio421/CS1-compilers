import ply.lex as lex

import cool_programs

from utils import tokenize

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


# List of token names

tokens = (
    reserved_words["class"],
    reserved_words["else"],
    reserved_words["fi"],
    reserved_words["if"],
    reserved_words["in"],
    reserved_words["inherits"],
    reserved_words["isvoid"],
    reserved_words["let"],
    reserved_words["loop"],
    reserved_words["pool"],
    reserved_words["then"],
    reserved_words["while"],
    reserved_words["case"],
    reserved_words["esac"],
    reserved_words["new"],
    reserved_words["of"],
    reserved_words["not"],
    bool_const,
    "assignment",
    "plus",
    "comma",
    "semicolon",
    "identifier",
    "integer",
    "STR_CONST",
    "symbol",
    "newline",
    "whitespace",
)


t_assignment = "="

t_plus = "\+"

t_comma = ","
t_semicolon = ";"
t_symbol = "[:{}\(\)]"

t_whitespace = "[ \n\f\r\t\v]"


def t_identifier(t):
    r"[_a-zA-Z][_a-zA-Z0-9]{0,30}"
    t.type = reserved_words.get(t.value, "identifier")
    t.value = value_lookup(t.value)
    return t


def t_integer(t):
    r"[0-9]+"
    t.value = int(t.value)
    return t


def t_STR_CONST(t):
    r'".*"'
    t.value = t.value.replace('"', '')
    return t


def t_newline(t):
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



