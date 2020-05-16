''' Реализовать функцию my_func(), которая принимает три позиционных аргумента,
  и возвращает сумму наибольших двух аргументов. '''

# функция громоздкая, т.к. допускается ввод символов пользователем и задание аргументов перечислением чисел
def my_func(*args):
    my_list = [*args]
    if len(my_list) == 1:
        if type(*args) is list:
            my_list = my_list.pop(0)
            if len(my_list) < 3:
                print('вы ввели менее 3-х чисел!!!')
                return
        else:
            print('вы ввели менее 3-х чисел!!!')
            return
    list_max = []
    while len(list_max) < 2:
        list_max.append(max(my_list))
        my_list.remove(max(my_list))
    print(list_max,'is max')
    return sum(list_max)


list_arg = []
print('Введите не меньше трех чисел раделенных пробелом')
my_arg = input().strip().split(' ')
for el in my_arg:
    try:
        list_arg.append(int(el))
    except ValueError:
        if len(list_arg) < 3:
            print('Вы ввели менее 3-х чисел')
        break

print(my_func(list_arg))
print('************************')
print(my_func(10,20,30,50,10,100))