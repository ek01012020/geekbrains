'''
Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу. Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.
'''

class Square:
    def __init__(self, cell):
        self.cell = cell

    def __str__(self):
        return str(self.cell)

    def __add__(self, other):
        return Square(self.cell + other.cell)

    def __sub__(self, other):
        if self.cell != other.cell:
            return Square(self.cell - other.cell)
        else:
            return 'В клетках одинаковое количество ячеек!'

    def __mul__(self, other):
        return Square(self.cell * other.cell)

    def __truediv__(self, other):
        return Square(self.cell / other.cell)

    def make_order(self, count_el):
        content = self.cell
        str_order = ''
        while content > count_el:
            str_order = str_order + '*' * count_el + '\n'
            content -= count_el
        if content > 0:
            str_order = str_order + '*' * content
        return str_order

s_1 = Square(12)
s_2 = Square(3)
print(s_1 + s_2)
print(s_1.make_order(5))
print((s_2 + s_1).make_order(4))
print(s_1 - s_2)
print(s_2 - s_1)
s_3 = Square(3)
print(s_2 - s_3)
print(s_2 / s_3)
print(s_2 * s_3)