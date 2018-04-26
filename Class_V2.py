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
        print('Mmm milk')


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
    def __init__(self, name, age, say):
        super().__init__(name, age)
        self.say = say


class Chicken(Birds):
    def eggs(self):
        print('Куры это не только мясо, но и яйца')


class Geese(Birds):
    def geese_meat(self):
        print('Гуси гуси га га га')


burenka = Cows('burenka', 4)
gavrusha = Cows('Gavrusha', 0.5)
darkwing_duck = Ducks('Darkwing Duck', 9, "I am the terror that flaps in the night!")
some_duck = Ducks('Duck', 1, 'quack quack')
pig = Pigs('pig', 2)
#print("Name: {} \nAge: {}\n".format(burenka.name, burenka.age))
#print("Name: {} \nAge: {} \nSay: {}\n".format(darkwing_duck.name, darkwing_duck.age, darkwing_duck.say))
#print("Name: {} \nAge: {}\n".format(gavrusha.name, gavrusha.age))
#print("Name: {} \nAge: {} \nSay: {}\n".format(some_duck.name, some_duck.age, some_duck.say))
#burenka.got_milk()
