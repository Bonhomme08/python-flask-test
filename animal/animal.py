class Animal:
    animal_type = ""
    sentence = ""
    favotire_food = []

    def __init__(self, name):
        self.name = name
        self.my_favorite_food = []

    def talk(self):
        return self.sentence
    
    def tell_a_story(self):
        return "Hello, I am a {animal} and my name is {name}.".format(animal=self.animal_type, name=self.name)
    
    def __str__(self):
        return self.name


class Dog(Animal):
    animal_type = "canine"
    sentence = "Woof !"
    favotire_food = ['Steaks', 'Hamburgers', 'Ice Cream']

    #def __init__(self, name):
    #    super(Dog, self).__init__(name)


class Cat(Animal):
    animal_type = "feline"
    sentence = "Meow !"
    favotire_food = ['Milk', 'Fish', 'Shrimps']

    #def __init__(self, name):
    #    super(Cat, self).__init__(name)

class Tiger(Animal):
    animal_type = "feline"
    sentence = "Rwarr !"
    favotire_food = ['Zebras', 'Stuff', 'Gazelle']
