#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке
def main5():
    zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

    # посадите медведя (bear) между львом и кенгуру
    #  и выведите список на консоль
    # TODO здесь ваш код
    zoo.insert(1, 'bear')

    print(zoo)

    # добавьте птиц из списка birds в последние клетки зоопарка
    birds = ['rooster', 'ostrich', 'lark', ]
    #  и выведите список на консоль
    # TODO здесь ваш код
    kletka = zoo + birds
    print(kletka)
    # уберите слона
    #  и выведите список на консоль
    # TODO здесь ваш код
    kletka.pop(3)
    print(kletka)
    # выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
    # Номера при выводе должны быть понятны простому человеку, не программисту.
    # TODO здесь ваш код
    lion_cage = kletka.index('lion') + 1
    lark_cage = kletka.index('lark') + 1
    return (f'лев сидит в клетке под номером {lion_cage}, а жаваронок находится в клетке под номером {lark_cage}')
if __name__ == '__main__':
    print(main5())