'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.'''
my_list = ['зима', 'весна', 'лето', 'осень']
my_dict = dict(k0='зима', k1='весна', k2='лето', k3='осень')
month = int(input('введите месяц в виде целого числа от 1 до 12: '))
if (month > 0) and (month < 13):
    month = month // 3
    if month == 4:
        month = 0
    print('Это ответ списка - ', my_list[month])
    str = 'k' + str(month)
    print('Это ответ словаря - ', my_dict.get(str))
else:
    print('вы указали недопустимое значение')
