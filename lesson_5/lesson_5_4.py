'''Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
'''
my_dict = {'1': 'один', '2': 'два', '3': 'три', '4': 'четыре'}
f_new = open('task_4_new.txt', 'w', encoding='utf-8')
with open('task_4.txt', encoding='utf-8') as f:
    for line in f:
        my_list = line.split()
        for i, el in enumerate(my_list):
            my_list[0] = my_dict.get(my_list[2])
        f_new.write(' '.join(my_list) + '\n')
f_new.close()