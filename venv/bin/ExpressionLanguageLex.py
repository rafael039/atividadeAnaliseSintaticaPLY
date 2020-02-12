# -------------------------
# ExpressionLanguageLex.py
#----------------------

import ply.lex as lex
tokens = ('COMMA', 'SOMA', 'ID', 'NUMBER', 'VEZES', 'POT', 'LPAREN', 'RPAREN',
'IGUAL',)
t_IGUAL= r'='
t_SOMA = r'\+'
t_VEZES = r'\*'
t_POT = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_ID = r'[a-zA-Z_][a-zA-Z_0-9]*'
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])

t.lexer.skip(1)
lexer = lex.lex()
#
# # Test it out
data = '''
3 + 4 ^ 10 + 20 *2 = chamada(a, b, 3)
'''
lexer.input(data)