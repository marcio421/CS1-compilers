class ListOfTokens(list):

    def __str__(self):
        # print each element on a line
        st = ""
        for element in self:
            element_as_str = str(element)
            line = element_as_str + "\n"
            st += line
        return st


def tokenize(lexer, data):

    lexer.input(data)

    tokens = ListOfTokens([])
    while True:
        tok = lexer.token()
        if not tok:
            break
        tokens.append(tok)
    return tokens
