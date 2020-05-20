'''Создать  текстовый  файл  (не  программно),  построчно  записать  фамилии  сотрудников  и
величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее  
20  тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода
сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
'''

with open('task_3.txt', encoding='utf-8') as f:
    my_staff = f.read().splitlines()
    print([my_str[:my_str.find(' ')] for my_str in my_staff if float(my_str[my_str.find(' ') + 1:]) < 20000])
    print(sum([float(my_str[my_str.find(' ') + 1:]) for my_str in my_staff]) / len(my_staff))