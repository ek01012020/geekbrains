'''Реализовать  скрипт,  в  котором  должна  быть  предусмотрена  функция  расчета  заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час)  +  премия.
Для  выполнения  расчета  для  конкретных  значений  необходимо  запускать скрипт с параметрами.'''
from sys import argv

script_mane, production, wage, award = argv
salary = lambda production, wage, award: (int(production) * int(wage)) + int(award)
print(salary(production, wage, award))