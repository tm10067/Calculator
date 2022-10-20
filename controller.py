import view
import model
import expression

def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            view.error_value()

def input_operation(enter):
    while True:
        expr = input(enter)
        if expr:
            return expr
        else:
            view.error_value()

def start_calc():
    while True:
        view.print_menu()
        mode = input("выберите действие: ")
        if mode == "1":
            expression.start_expr_calc()
            break
        elif mode == "2":
            model.init_calc()
            break
        elif mode == "0":
            break
        else: 
            view.error_value()
       
