'''Представлен  список  чисел.
Необходимо  вывести  элементы  исходного  списка,  значения которых больше предыдущего элемента.'''

my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
list_new = [my_list[ind+1] for ind, el in enumerate(my_list) if (ind < (len(my_list)-1)) and (my_list[ind+1] > my_list[ind])]
print(list_new)
#[12, 44, 4, 10, 78, 123]