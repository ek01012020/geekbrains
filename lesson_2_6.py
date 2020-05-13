'''*Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
Каждый кортеж хранит информацию об отдельном товаре.
В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения).
Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {"название": "компьютер", "цена": 20000, "количество": 5, "eд": "шт."}),
    (2, {"название": "принтер", "цена": 6000, "количество": 2, "eд": "шт."}),
    (3, {"название": "сканер", "цена": 2000, "количество": 7, "eд": "шт."})
]
Необходимо собрать аналитику о товарах.
Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    "название": ["компьютер", "принтер", "сканер"],
    "цена": [20000, 6000, 2000],
    "количество": [5, 2, 7],
    "ед": ["шт."]
}'''

my_list = []
i = 1
while True:
    my_tuple = []
    my_tuple.append(i)
    my_dict = dict(name=input('введите название товара: '))
    my_dict.update(price=input('введите цену товара: '))
    my_dict.update(count=input('введите количество товара: '))
    my_dict.update(unit=input('введите ед.измерения товара: '))
    my_tuple.append(my_dict)
    my_list.append(tuple(my_tuple))
    if input('выйти из добавления товаров? Y+Enter ').upper() == 'Y':
        break
    i = i + 1

analytics = {}
for product in my_list:
    characteristic = product[1]
    for key, value in characteristic.items():
        characteristicValue = analytics.get(key)
        if characteristicValue is None:
            analytics[key] = [value]
        else:
            setCharacteristic = set(characteristicValue)
            setCharacteristic.add(value)
            analytics[key] = list(setCharacteristic)
print(f"Аналитика: {analytics}")