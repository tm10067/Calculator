import model
import view
import logger

expr = ''
expr_norm = []

def init_expr():
    global expr
    print(expr)
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
    print(expr_norm)

def extract_simple():
    global expr_norm
    print(expr_norm)
    while len(expr_norm) > 1:
        print(expr_norm)
        if "(" in expr_norm and ")" in expr_norm:
            start_pos = 0
            end_pos = 0
            for i in range(len(expr_norm)):
                if expr_norm[i] == "(":
                    start_pos = i + 1
                elif start_pos != 0 and expr_norm[i] == ")":
                    end_pos = i
                    expr_simple = expr_norm[start_pos : end_pos]
                    model.total = calculate_simple(expr_simple)
                    expr_norm = expr_norm[0 : start_pos - 1] + [str(model.total)] + expr_norm[end_pos + 1 : len(expr_norm)] 
                    break
        else:
            calculate_simple(expr_norm)

def calculate_simple(expr_simple: list):
    while len(expr_simple) > 1:
        print(expr_simple)
        for j in range(len(expr_simple)):
            if expr_simple[j] == '*' or expr_simple[j] == '/':
                model.first = int(expr_simple[j - 1])
                model.second = int(expr_simple[j + 1])
                model.operation()
                expr_simple[j - 1] = str(model.total)
                expr_simple.pop(j)
                expr_simple.pop(j)
                print(model.first)
                print(model.second)
                print(model.total)
                print(expr_simple)
                break
            if expr_simple[j] == "+" or expr_simple[j] == "-":
                model.first = int(expr_simple[j - 1])
                model.second = int(expr_simple[j + 1])
                model.operation()
                expr_simple[j - 1] = str(model.total)
                expr_simple.pop(j)
                expr_simple.pop(j)
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
    
# expr = ''
# expr_norm = []

# def init_expr():
#     global expr
#     expr = input_expr('Введите выражение: ')

# def input_expr(enter):
#     while True:
#         expr = input(enter)
#         if expr:
#             return expr
#         else:
#             view.error_value()

# def normalise_expression(expr: str):
#     global expr_norm
#     expr_norm = expr.strip().replace("+"," + ").replace("-"," - ").replace("*"," * ").replace("/"," / ").replace("("," ( ").replace(")"," ) ").split(" ")
#     expr_norm = expr_norm.remove(" ")
#     print (expr_norm)
#     return expr_norm

# def extract_simple(expr_norm: list):
#     while 
#         if "(" in expr_norm and ")" in expr_norm:
#             start_pos = 0
#             end_pos = 0
#             for i in range(len(expr_norm)):
#                 if i == "(":
#                     start_pos = i + 2
#                 elif start_pos != 0 and i == ")":
#                     end_pos = i - 2
#                     expr_simple = expr_norm[start_pos : end_pos]
#                     print(expr_simple)
#                     calculate_simple(expr_simple)
#                     expr_norm = expr_norm[0 : start_pos - 3] + f"{expr_simple}" + expr_norm[end_pos + 3 : len(expr_norm)] 
#                     break
#                 else:
#                     break
#     else:
#         calculate_simple(expr_norm)
#     return expr_norm

# def calculate_simple(expr_simple: list):
#     while len(expr_simple) > 1:
#         for j in range(len(expr_simple)):
#             if j == "*" or "/":
#                 model.first = int(expr_simple[j - 2])
#                 model.second = int(expr_simple[j + 2])
#                 model.ops = j
#                 model.operation()
#                 expr_simple[j - 2] = str(model.total)
#                 expr_simple.pop(j - 1, j, j + 1, j + 2)
#                 print(expr_simple)
#                 break
#             if j == "+" or "-":
#                 model.first = int(expr_simple[j - 2])
#                 model.second = int(expr_simple[j + 2])
#                 model.ops = j
#                 model.operation()
#                 expr_simple[j - 2] = str(model.total)
#                 expr_simple.pop([j - 1],[j],[j + 1],[j + 2])
#                 print(expr_simple)
#                 break
#     return expr_simple

# def calculate():
#     global expr
#     normalise_expression()
#     extract_simple(expr_norm)
#     print(expr_norm)
#     model.total = int(expr_norm[0])
#     logger.logger(f'{expr} = {model.total}') 

# def start_expr_calc():
#     global expr
#     init_expr()
#     calculate()
#     view.print_expr_total(expr, model.total)
