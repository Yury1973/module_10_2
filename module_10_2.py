"""
Задача "За честь и отвагу!"
"""

from threading import Thread

from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy_power = 100
        battle_days = 0
        print(f'{self.name}, на нас напали!')
        for i in range(1, enemy_power):
            if enemy_power > 0:
                enemy_power -= self.power
                battle_days += 1
                if battle_days == 1:
                    day = 'день'
                elif battle_days in range(2, 5):
                    day = 'дня'
                else:
                    day = 'дней'
                print(f'{self.name} сражается {battle_days} {day}..., осталось {enemy_power} воинов.')
                sleep(1)
                if enemy_power <= 0:
                    print(f'{self.name} одержал победу спустя {battle_days} {day}!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')
