import logger
import model
import view


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
            return a
        else:
            view.error_value()

def operation():
    while True:
        if model.ops == '+':
            model.total = model.first + model.second
            break
        elif model.ops == '-':
            model.total = model.first - model.second
            break
        elif model.ops == '*':
            model.total = model.first * model.second
            break
        elif model.ops ==  '//':
            while model.second == 0:
                print('На ноль делить нельзя!')
                model.init_second()
            model.total = model.first // model.second
            break
        else:
            view.error_value()
            break
    logger.logger(f'{model.first} {model.ops} {model.second} = {model.total}') 