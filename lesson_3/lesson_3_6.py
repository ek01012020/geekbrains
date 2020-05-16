''' Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func().'''


int_func = lambda arg_str: arg_str.capitalize()


print('Введите строку для редактирования')
my_str = input()
str_new = ''
position = 0
while position != -1:
    position = my_str.find(' ')
    my_tuple = my_str.partition(' ')
    str_new = str_new + int_func(my_tuple[0]) + my_tuple[1]
    my_str = my_str[position+1:]
print(str_new)