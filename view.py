import logger

def error_value():
    logger.logger('Ошибка ввода данных')
    return print('Ошибка ввода данных')

def print_total(total):
    return print(f'Результат: {total}')

def print_expr_total(expr, total):
    return print(f'{expr} = {total}')

def print_menu():
    print ("1: для ввода выражения нажмите 1")
    print ("2: для режима калькулятора нажмите 2")
    print ("0: для выхода нажмите 0")