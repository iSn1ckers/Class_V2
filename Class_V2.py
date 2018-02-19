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


class Cows(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def got_milk(self):
        print('Благодаря корове у вас будет молоко')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Goats(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def got_milk(self):
        print('Козы как и коровы дают молоко')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Sheep(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def wool(self):
        print('Благодаря овцам у вас будет шерсть')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Pigs(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def meat(self):
        print('Свинина, ням ням')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Ducks(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def duck_meat(self):
        print('Утиное мясо очень вкусное, да и перья пригодятся')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Chickens(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def eggs(self):
        print('Куры это не только мясо, но и яйца')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


class Geese(Animal):
    def __init__(self, name, age, speech):
        Animal.__init__(self, name, age)
        self.speech = speech

    def geese_meat(self):
        print('Гуси гуси га га га')

    def __str__(self):
        return 'Животное: {0}\n Возраст: {1}\n "Говорит": {2}'.format(self.name, self.age, self.speech)


c = Geese(input('Как зовут вашего питомца?'), input('Сколько ему лет?'), input('Какой звук он издает?'))
# c.name = input()
# c.age = input()
# c.speech - input()
print (c)
c.geese_meat()
