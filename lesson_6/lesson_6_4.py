'''Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''

class Car:
    is_police = False

    def __init__(self, color, name, speed):
        self.color = color
        self.name = name
        self.speed = speed

    def go(self):
        if self.speed > 0:
            print(f'Машина {self.name} поехала')

    def stop(self):
        if self.speed == 0:
            print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        if direction == 'left':
            print(f'Машина {self.name} повернула налево')
        elif direction == 'right':
            print(f'Машина {self.name} повернула направо')
        elif direction == 'straight':
            print(f'Машина {self.name} поехала прямо')
        elif direction == 'turn':
            print(f'Машина {self.name} развернулась')

    def show_speed(self):
        print(f'Скорость машины - {self.speed}')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Превышение скорости! {self.speed}! Допустимая скорость 60')

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Превышение скорости! {self.speed}! Допустимая скорость 40')

class PoliceCar(Car):
    is_police = True

car_1 = TownCar('red', 'Ferrari', 120)
car_1.go()
print(f'скорость машины - {car_1.speed}')
car_1.show_speed()
print(f'{car_1.name} полицейская машина - {car_1.is_police}')
car_2 = PoliceCar('white', 'Lada', 100)
car_2.go()
car_2.turn('left')
print(f'{car_2.name} полицейская машина - {car_2.is_police}')
car_2.show_speed()
car_3 = WorkCar('orange', 'KAMAZ', 0)
car_3.stop()
car_3.go()
car_3.speed = 50
car_3.show_speed()
print(f'{car_3.name} полицейская машина - {car_3.is_police}')
