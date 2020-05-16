'''Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,'''


from itertools import count, cycle

start = int(input('введите с какого числа начанается генерация -  '))
finish = int(input('введите сколько чисел генерировать -  ')) + start - 1
for el in count(start):
    if el > finish:
        break
    else:
        print(el)

'''б) итератор, повторяющий элементы некоторого списка, определенного заранее.'''

my_list = [1, 2, 3]
num_repeat = int(input('введите сколько раз повторить вывод всех элементов списка -  ')) * len(my_list)
for el in cycle(my_list):
    if num_repeat > 0:
        print(el)
    else: break
    num_repeat = num_repeat - 1