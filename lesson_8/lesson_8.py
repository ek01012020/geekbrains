from random import randint
class Card:
    def __init__(self):
        self.my_list = []
        self.my_dict = {}
        self.numerics = {el for el in range(1, 91)}
        i = 0
        while i < 15:
            while True:
                new_value = self.generic_next()
                key = new_value // 10
                value = self.my_dict.get(key)
                if value is None:
                    self.my_dict[key] = 1
                    self.my_list.append(new_value)
                    i += 1
                    break
                else:
                    if value == 2:
                        continue
                    else:
                        self.my_dict[key] += 1
                        self.my_list.append(new_value)
                        i += 1
                        break
        #self.my_list.sort()

    def generic_next(self):
        while True:
            number = randint(1, 90)
            if number in self.numerics:
                self.numerics.remove(number)
                return number

    def __str__(self):
        self.my_str = ''
        for ind, el in enumerate(self.my_list, start=1):
            if ind % 5 == 0:
                self.my_str = self.my_str + str(el) + '\n'
            else:
                self.my_str = self.my_str + str(el) + ' '
        return f'{self.my_str}'

class Player:
    def __init__(self, name):
        self.name = name
        self.my_card = Card()

    def player_step(self, paso):
        print(paso)
        answer = input('У вас есть бочонок? y/n')
        if self.my_card.my_list.count(paso) != 0 and answer == 'y':
                self.my_card.my_list[self.my_card.my_list.index(paso)] = '-'
        elif (self.my_card.my_list.count(paso) != 0 and answer == 'n') or (self.my_card.my_list.count(paso) == 0 and answer == 'y'):
                print('Game over')
                exit(Player)
        else: pass
        return f'new_card \n{self.my_card}'


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
        print(player.player_step(b.el_paso()))
    print('Exit? y/n')

