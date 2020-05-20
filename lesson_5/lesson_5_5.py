'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''
from random import randint

with open('task_5.txt', 'w', encoding='utf-8') as f:
    my_list = [str(randint(1,10)) for el in range(10)]
    f.write(' '.join(my_list))
with open('task_5.txt') as f:
    print(sum([int(el) for el in f.read().split()]))