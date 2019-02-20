# https://docs.python-guide.org/dev/virtualenvs/
# http://flask.pocoo.org/

# from flask import Flask
# from .stuff.animal import Dog, Cat

# app = Flask(__name__)


class Animal:
    def __init__(self):
        self.sentence = ""

    def talk(self):
        return self.sentence


class Dog(Animal):
    def __init__(self):
        super(Dog, self).__init__()
        self.sentence = "Woof !"


class Cat(Animal):
    def __init__(self):
        super(Cat, self).__init__()
        self.sentence = "Meow !"


# @app.route("/")
def hello():
    cat = Cat()
    dog = Dog()
    return "The dog says: {} and the cat says: {}".format(cat.talk(), dog.talk())


print(hello())
