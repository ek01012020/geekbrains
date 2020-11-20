from random import randint
class Card:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.count_paso = 0
        self.numerics = {el for el in range(1, 91)}
        for row in self.matrix:
            i = 0
            while i < 5:
                new_value = self.generic_next()
                if new_value == 90:
                    column_number = 8
                else:
                    column_number = new_value // 10
                if row[column_number] == 0:
                    row[column_number] = new_value
                else:
                    continue
                self.count_paso += 1
                i += 1
        print(self.matrix)

    def generic_next(self):
        while True:
            number = randint(1, 90)
            if number in self.numerics:
                self.numerics.remove(number)
                return number

    def contain_paso(self, paso):
        for x, row in enumerate(self.matrix):
            for y, value in enumerate(row):
                if value == paso:
                    self.matrix[x][y] = 0
                    self.count_paso -= 1
                    return True
        return False

    def __str__(self):
        all_str = ''
        for row in self.matrix:
            row_str = ''
            for value in row:
                if value == 0:
                    row_str += "  "
                else:
                    row_str += str(value) + " "
            all_str += row_str + '\n'
        return all_str


class Player:
    def __init__(self, name):
        self.name = name
        self.my_card = Card()

    def player_step(self, paso):
        print(paso)
        answer = input('У вас есть бочонок? y/n')
        contain_paso = self.my_card.contain_paso(paso)
        if contain_paso == True and answer == 'y':
            print(f'new_card \n{self.my_card}')
        elif (contain_paso == True and answer == 'n') or (self.my_card.count_paso == 0 and answer == 'y'):
            print('Game Over')
            exit(player)
        else:
            pass

class Base:
    def __init__(self):
        self.my_base = {el for el in range(1, 91)}

    def el_paso(self):
        while True:
            paso = randint(1, 90)
            if paso in self.my_base:
                self.my_base.remove(paso)
                return paso

print('Exit? y/n')
b = Base()
while input() != 'y':
    player = Player('Helen')
    print(player.my_card)
    while player.my_card != 0:
        player.player_step(b.el_paso())
    print('Exit? y/n')

