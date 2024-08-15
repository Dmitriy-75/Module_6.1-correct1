class Animal:
    alive = True
    fed = False

    def eat(self, food):

        if food.edible:
            print(f'{self.name} съел {food.name}')
            Animal.fed = True
        else:
            print(f'{self.name}  не стал есть {food.name}')
            Animal.alive = False


class Mammal(Animal):
    def __init__(self, name):
        self.name = name


class Predator(Animal):
    def __init__(self, name):
        self.name = name


class Plant:
    edible = False


class Flower(Plant):
    def __init__(self, name):
        self.name = name


class Vegetables(Plant):
    def __init__(self, name):
        self.name = name


Vegetables.edible = True

a1 = Predator('Волк с Ну погоди')
a2 = Mammal('Заинька серенький (типа с песни)')
p1 = Flower('Ромашка')
p2 = Vegetables('Морковка')


print(a1.name)
print(p1.name)

print(a1.alive)   # Голодный волк жив?
print(a2.fed)     # а зайка сыт?

a1.eat(p1)
a2.eat(p2)

print(a1.alive)    # Голодный волк выжил, отказавшись от ромашки?
print(a2.fed)      # Наелся зайка морковкой?















