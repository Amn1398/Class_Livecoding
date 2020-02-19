class Meal:
    def __init__(self, name, calories =250):
        self.name = name
        self.calories = calories

class Animal:
    def __init__(self):
        self.meals_eaten = []

    def eat(self, food: Meal):
        self.meals_eaten.append(food)
        print("I eat {}".format(food.name))

    def play(self):
        print("playtime!")

class Dog(Animal):
    def __init__(self, name = "DEFALTO", age: float = 3.0)
        super.__init__()
        self.age = age
        self.name = name

    def bark(self, loudness):
        if loudness < 0.5:
            print("Ruff!")
        else:
            print("BOWOWOWOWOW")

        def snuggle():
            print("")

class Cat(Animal):
    def __init__(self):
        self.lives = 9

    def purr(self):
        print("Purr")

    def walk(self):
        print("Bebop around.")

    def play(self):
        self.play()
        print("I pounce")

class Chiweenie(Dog):
    def __init__(self):
        super().__init__(name, age)
        self.napolean_complex = True