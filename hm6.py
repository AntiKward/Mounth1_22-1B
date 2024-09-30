def is_even(a):
  if a % 2 == 0:
    print(f'{a} True')
  else:
    print(f'{a} False')
is_even(int(input('')))

def list_py():
  my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  list_two = []
  for i in my_list:
    if i % 2 == 0:
      print(f'{i} чётное число',end = ' ')
      list_two.append(i)
    else:
      pass
    
list_py()
