import controller
import view
import logger

first = 0
second = 0
ops = ''
total = 0

def init_first():
    global first
    first = controller.input_integer('Введите число: ')

def init_second():
    global second
    second = controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total(total)
        return True

def operation():
    global total
    while True:
        if ops == '+':
            total = first + second
            break
        elif ops == '-':
            total = first - second
            break
        elif ops == '*':
            total = first * second
            break
        elif ops ==  '/':
            while second == 0:
                print('На ноль делить нельзя!')
                init_second(second)
            total = first // second
            break
        else:
            view.error_value()
            break
    logger.logger(f'{first} {ops} {second} = {total}') 

def init_calc():
    init_first()
    while True:
        if init_ops():
            break
        init_second()
        operation()
        view.print_total(total)
        global first
        first = total