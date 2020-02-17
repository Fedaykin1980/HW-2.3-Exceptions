a = input('Введите операнд (+, -, *, /):')
assert a in ['+', '-', '*', '/'], 'Вы ввели неправильно операнд'

b = input('Введите первое число:')
try:
    b != int(b)
except ValueError:
    print('Вы ввели не число')
finally:
    print('Попробуйте заново')
    exit()

c = input('Введите второе число:')
try:
    c != int(c)
except ValueError:
    print('Вы ввели не число')
finally:
    print('Попробуйте заново')
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