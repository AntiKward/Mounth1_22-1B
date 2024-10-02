# f = open('asd.txt', 'w', encoding='UTF-8')
# f.write('дыфдыв')
# print(f)
# f.close()
# a = open('asd.txt', 'r', encoding='UTF-8')
# s = a.read()
# print(s)


s = str(input('имя: '))
if s == s:
  a = open('name.txt', 'w')
  a.write(f'{s}')
  a.close()
  v = open('name.txt', 'r')
  reading = v.read()
  print(f'{reading}\n')
  v.close()
else:
  print('Ошибка')

# def add_student(name, age):
#   with open('student.txt', '+a' ) as f:
#     f.write(f'{name} - {age}\n')
#     if name in 'student.txt':
#       print('Этот пользователь еще не в базе данных')
#     else:
#       print('Этот пользователь внутри базы данных')

    
# add_student(name = str(input('Введите имя: ')),age = int(input('Введите возраст: ')))

# def main():
#   print('1 - добавить, 2 - все студенты')
#   choise = int(input('Введите'))
  