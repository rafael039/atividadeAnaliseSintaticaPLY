# -------------------------
# ExpressionLanguageParser.py
#----------------------
import ply.yacc as yacc
import ply.lex as lex
from ExpressionLanguageLex import tokens

def p_exp_soma(p):
    '''exp : exp SOMA exp1
        | exp1'''
def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
        | exp2'''

def p_exp2_potencia(p):
    '''exp2 : exp3  POT exp2
        | exp3'''

def p_exp3_chamada(p):
    '''exp3 : call
        | assign
        |num
        |id  '''

def p_call_chamadaParam(p):
    '''call : id LPAREN params RPAREN
        | id LPAREN RPAREN '''

def p_params_parametro(p):
    '''params: id COMMA params
        |id'''

def p_assign_atribuicao(p):
    '''assign: id IGUAL exp'''

parser = yacc.yacc()

result = parser.parse(debug=True)