name = 'Geeks'
password = '2024'

user_name = input('Введите свой user_name: ')
user_password = input('Введите свой user password: ')

if user_name == name and user_password == password:
    print('Вы успешно вошли')
elif user_name != name and user_password != password:
    print('Вы неправильно ввели никнейм и пароль')
elif user_name != name:
    print('Вы неправильно ввели никнейм')
elif user_password != password:
    print('Вы неправильно ввели пароль')

