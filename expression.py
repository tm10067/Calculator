import model
import view

expr = ''

def init_expr():
    global expr
    expr = input_expr('Введите выражение: ')

def input_expr(enter):
    while True:
        expr = input(enter)
        if ['+', '-', '*', '/'] in expr:
            return expr
        else:
            view.error_value()



def normalise_expression(expr: str):
    expr_norm = expr.strip().replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").replace("("," ( ").replace(")"," ) ").split("")
    print (expr_norm)
    return expr_norm

def extract_simple(expr_norm):
    return 0

def calculate_simple(expr_simple):
    return 0

def calculate(expr):
    normalise_expression(expr)

