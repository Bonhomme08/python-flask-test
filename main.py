# https://docs.python-guide.org/dev/virtualenvs/
# http://flask.pocoo.org/

#from flask import Flask
from animal.animal import Cat, Dog, Tiger
from misc.decorators import print_line
from operator import add

#app = Flask(__name__)

animal_list = [Cat('Sushy'), Dog('Fido'), Tiger('Incineroar')]

#@app.route("/")
def hello():
    test_simple_loop()
    test_a_comprehensive_list_digging()
    test_a_comprehensive_list_with_condition()
    test_a_map_1()
    test_a_map_2()

    return ""

@print_line
def test_simple_loop():
    for animal in animal_list:
        print(animal.tell_a_story())

@print_line
def test_a_comprehensive_list_digging():
    name_list = [animal.name for animal in animal_list]

    for name in name_list:
        print(name)

@print_line
def test_a_comprehensive_list_with_condition():
    filtered_list = [animal for animal in animal_list if animal.animal_type == "feline"]

    for animal in filtered_list:
        print(animal.name)

@print_line
def test_a_map_1():
    list(map(lambda a_str: print("Sir {}".format(a_str)), animal_list))
    

@print_line
def test_a_map_2():
    pass
    #print(list(map(add, [1, 2, 3], [4, 5, 6])))
    #a_new_list = list(map(lambda a_str: "Sir {}".format(a_str), animal_list))
    #print(a_new_list)


hello()
