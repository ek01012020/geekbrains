''' Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''

my_str = ''
summ = 0
print('Для завершения программы введите любую букву')


def my_sum(arg_str):
    my_list = arg_str.split(' ')
    for el in my_list:
        my_list.insert(my_list.index(el), int(my_list.pop(my_list.index(el))))
    return sum(my_list)


while True:
    try:
        my_str = input('введите строку чисел для суммирования ').strip(' ')
        summ += my_sum(my_str)
    except ValueError:
        my_list = my_str.split(' ')
        list_new = []
        for el in my_list:
            if el.isdigit():
                list_new.append(el)
            else:
                break
        if list_new != []:
            summ += my_sum(' '.join(list_new))
        break
    finally:
        print(summ)