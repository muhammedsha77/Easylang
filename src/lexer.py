import ply.lex as lex


class Mylexer:
    # List of token names
    tokens = (
        'LET', 'FUNCTION', 'RETURN', 'ELSE', 'FOR', 'WHILE',
        'IDENTIFIER', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
        'MOD', 'LT', 'GT', 'LEQ', 'GEQ', 'EQ', 'NEQ', 'LPAREN', 'RPAREN', 'LBRACE',
        'RBRACE', 'NEWLINE', 'SEMICOLON', 'IF', 'ASSIGN', 'MULTICOMMENT', 'COMMENT'
    )

    # Regular expression rules for simple tokens
    t_ASSIGN = r'='
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_TIMES = r'\*'
    t_DIVIDE = r'/'
    t_MOD = r'%'
    t_LT = r'<'
    t_GT = r'>'
    t_LEQ = r'<='
    t_GEQ = r'>='
    t_EQ = r'=='
    t_NEQ = r'!='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_NEWLINE = r'\n+'
    t_SEMICOLON = r';'

    # semantic Action
    @staticmethod
    def t_LET(token):
        r'let'
        token.type = 'LET'
        return token

    @staticmethod
    def t_FUNCTION(token):
        r'fn'
        token.type = 'FUNCTION'
        return token

    @staticmethod
    def t_RETURN(token):
        r'return'
        token.type = 'RETURN'
        return token

    @staticmethod
    def t_IF(token):
        r'if'
        token.type = 'IF'
        return token

    @staticmethod
    def t_ELSE(token):
        r'else'
        token.type = 'ELSE'
        return token

    @staticmethod
    def t_FOR(token):
        r'for'
        token.type = 'FOR'
        return token

    @staticmethod
    def t_WHILE(token):
        r'while'
        token.type = 'WHILE'
        return token

    @staticmethod
    def t_IDENTIFIER(token):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        return token

    @staticmethod
    def t_NUMBER(token):
        r'\d+'
        token.value = int(token.value)
        return token

    @staticmethod
    def t_MULTICOMMENT(token):
        r"'''(.|\n)*?'''"
        pass

    t_ignore = ' \t'  # Ignore spaces and tabs

    @staticmethod
    def t_COMMENT(token):
        r'\#.*'
        pass

    @staticmethod
    def t_error(token):
        print(f"Illegal character '{token.value[0]}' at line {token.lineno}")
        token.lexer.skip(1)

    @staticmethod
    def t_newline(token):
        r'\n+'
        token.lexer.lineno += len(token.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def test(self, data):
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            print(tok.type, tok.value, tok.lineno, tok.lexpos)


# Example usage of the lexer
if __name__ == '__main__':
    data = '''
    let x = 5 + 3.14; # variable
    if (x < 10) {
        return x;
    } else {
        return 0;
    }'''

    easylanglexer = Mylexer()
    easylanglexer.build()
    easylanglexer.test(data)

