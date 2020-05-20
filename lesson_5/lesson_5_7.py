'''Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать
данные о фирме: название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста.
'''
import json

with open('task_7.txt', encoding='utf-8') as f:
    my_dict = {}
    average_profit = []
    for line in f:
        my_list = line.split()
        for i, el in enumerate(my_list):
            my_dict[my_list[0]] = int(my_list[2]) - int(my_list[3])
            if int(my_list[2]) - int(my_list[3]) > 0:
                average_profit.append(int(my_list[2]) - int(my_list[3]))
average_profit = int(sum(average_profit) / len(average_profit))
my_list = [my_dict, {'average_profit':average_profit}]
print(my_list)
with open('task_7.json', 'w', encoding='utf-8') as f_json:
    json.dump(my_list, f_json)