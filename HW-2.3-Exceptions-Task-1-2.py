a, b, c = input('Введите пример +22: ')
assert a in ['+', '-', '*', '/'], 'Вы ввели неправильно операнд'

try:
    b != int(b)
    c != int(c)
except ValueError:
    print('Вы ввели не число')
    exit()

try:
    if a == '+':
        result = int(b) + int(c)
        print(result)
    elif a == '-':
        result = int(b) - int(c)
        print(result)
    elif a == '*':
        result = int(b) * int(c)
        print(result)
    elif a == '/':
        result = int(b) / int(c)
        print(result)
except ZeroDivisionError:
    print('На ноль делить нельзя')
except Exception:
    print('Что-то пошло не так o_O')
