'''Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
'''

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list
        self.new_list = []
        self.num_column = len(my_list[0])
        if my_list != []:
            for el in my_list:
                for num in el:
                    self.new_list.append(num)

    def __str__(self):
        my_str = ''
        for ind, el in enumerate(self.new_list, start=1):
            if ind % self.num_column == 0:
                my_str = my_str + str(el) + '\n'
            else:
                my_str = my_str + str(el) + ' '
        return my_str

    def __add__(self, other):
        new_matrix = []
        new_line = []
        new_matrix_new = []
        for ind, el in enumerate(self.new_list):
            new_matrix.append(el + other.new_list[ind])
        i = 0
        for el in new_matrix:
            i += 1
            if i % self.num_column != 0:
                new_line.append(el)
            else:
                new_line.append(el)
                new_matrix_new.append(new_line)
                new_line = []
        return Matrix(new_matrix_new)


mat_1 = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
mat_2 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(mat_1)
print(mat_2)
print(mat_1 + mat_2)