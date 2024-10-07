def calculator():
    """Вот такие комменты надо оставлять"""
    numb_1 = int(input('Введите первое число: '))
    choice = input('Введите знак: ')
    numb_2 = int(input('Введите второе число: '))
    if choice == '+':
        return  numb_1 + numb_2
    elif choice == '-':
        return numb_1 - numb_2
    elif choice == '*':
        return numb_1 * numb_2
    elif choice == '/':
        return numb_1 / numb_2
    elif numb_1 or numb_2 == 0 and choice == '/':
        return 'Error'

print(calculator())

