'''Создать  текстовый  файл  (не  программно),  сохранить  в  нем  несколько  строк,  выполнить
подсчет количества строк, количества слов в каждой строке.'''

with open('task_2.txt', encoding='utf-8') as f:
    my_list = f.readlines()
print(f'Файл содержит строк - {len(my_list)}')
for i, el in enumerate(my_list):
    print(f'{i + 1} строка - слов {len(el.split())}')