# Домашнее задание к лекции 1.7 «Классы и их применение в Python»
# Необходимо реализовать классы животных на ферме:
#
# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
# Условия:
#
# Должен быть один базовый класс, который наследуют все остальные животные.
# Базовый класс должен определять общие характеристики и интерфейс.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cattle(Animal):
    hoofs = 4


class Birds(Animal):
    wings = 2


class Cows(Cattle):
    def got_milk(self):
        print('Благодаря корове у вас будет молоко')


class Goats(Cattle):
    def goat_milk(self):
        print('Козы как и коровы дают молоко')


class Sheeps(Cattle):
    def wool(self):
        print('Благодаря овцам у вас будет шерсть')


class Pigs(Cattle):
    def meat(self):
        print('Свинина, ням ням')


class Ducks(Birds):
    def duck_meat(self):
        print('Утиное мясо очень вкусное, да и перья пригодятся')


class Chicken(Birds):
    def eggs(self):
        print('Куры это не только мясо, но и яйца')


class Geese(Birds):
    def geese_meat(self):
        print('Гуси гуси га га га')



