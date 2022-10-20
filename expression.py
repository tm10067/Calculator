import model
import view
import logger

expr = ''
expr_norm = []

def init_expr():
    global expr
    expr = input_expr('Введите выражение: ')

def input_expr(enter):
    while True:
        expr = input(enter)
        if expr:
            return expr
        else:
            view.error_value()

def normalise_expression():
    global expr
    global expr_norm
    expr_norm = expr.replace(" ","").replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").replace("(","( ").replace(")"," )").split(" ")

def extract_simple():
    global expr_norm
    while len(expr_norm) > 1:
        if "(" in expr_norm and ")" in expr_norm:
            start_pos = 0
            end_pos = 0
            for i in range(len(expr_norm)):
                if expr_norm[i] == "(":
                    start_pos = i + 1
                elif start_pos != 0 and expr_norm[i] == ")":
                    end_pos = i
                    expr_simple = expr_norm[start_pos : end_pos]
                    calculate_simple(expr_simple)
                    expr_norm = expr_norm[0 : start_pos - 1] + [str(model.total)] + expr_norm[end_pos + 1 : len(expr_norm)] 
                    break
        else:
            calculate_simple(expr_norm)

def calculate_simple(expr_simple: list):
    while len(expr_simple) > 1:
        for j in range(len(expr_simple)):
            if expr_simple[j] == '*' or expr_simple[j] == '/':
                model.first = int(expr_simple[j - 1])
                model.second = int(expr_simple[j + 1])
                model.ops = expr_simple[j]
                model.operation()
                expr_simple[j - 1] = str(model.total)
                expr_simple.pop(j)
                expr_simple.pop(j)
                break
        for k in range(len(expr_simple)):
            if expr_simple[k] == "+" or expr_simple[k] == "-":
                model.first = int(expr_simple[k - 1])
                model.second = int(expr_simple[k + 1])
                model.ops = expr_simple[k]
                model.operation()
                expr_simple[k - 1] = str(model.total)
                expr_simple.pop(k)
                expr_simple.pop(k)
                break

def calculate():
    global expr_norm
    normalise_expression()
    extract_simple()
    model.total = int(expr_norm[0])
    logger.logger(f'{expr} = {model.total}') 

def start_expr_calc():
    init_expr()
    calculate()
    view.print_expr_total(expr, model.total)