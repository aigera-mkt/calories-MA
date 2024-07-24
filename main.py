# -*- encoding: utf-8 -*-

from __future__ import print_function
import sys
print(sys.version)

class SmartDiet:
    def __init__(self):
        self.food={}
        self.total_calories=0

    def register_food (self, name, calories):
        self.food[name]=calories

    def add_food (self,name,amount):
        self.total_calories += self.food['name']*amount

    def calculate(self):
        return self.total_calories

if __name__ == '__main__':

    food = {
        "Хлеб": 300,
        "Круассан": 450,
        "Курица": 300
    }
    diet = SmartDiet()
    for name, calories in food.items():
        diet.register_food(name, calories)
    while True:
        print("Выберите еду:")
        for name in food:
            print("\t" + name)
        name = input("Название: ")
        count = int(input("Количество: "))
        diet.add_food(name, count)
        print("Суммарная калорийность: " + str(diet.calculate()))