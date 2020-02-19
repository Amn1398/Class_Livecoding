from animals import Dog, Cat, Meal, Chiweenie

if __name__ == '__main__':
    charlie = Chiweenie("Chuck", 9)
    jules = Cat()
    import pdb; pdb.set_trace()
    meal = Meal("table scrapes", 200)

    charlie.eat(meal)
    jules.eat(meal)
    print(jules.lives)
    print(jules.meals_eaten)

    jules.play()
    charlie.play()