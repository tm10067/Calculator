import controller
import model
import view
import expression

def init_calc():
    model.init_first()
    while True:
        if model.init_ops():
            break
        model.init_second()
        controller.operation()
        view.print_total()
        model.first = model.total

while True:
    print ("1: для ввода выражения нажмите 1")
    print ("2: для режима калькулятора нажмите 2")
    print ("0: для выхода нажмите 0")
    mode = input("выберите действие: ")
    if mode == "1":
        expression.init_expr()
        break
    elif mode == "2":
        init_calc()
        break
    elif mode == "0":
        break
    else: 
        view.error_value()





