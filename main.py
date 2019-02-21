# https://docs.python-guide.org/dev/virtualenvs/
# http://flask.pocoo.org/
# https://www.bogotobogo.com/python/python_fncs_map_filter_reduce.php

from flask import Flask
from animal.animal import Cat, Dog, Tiger
from misc.decorators import print_line
from functools import reduce
from misc.custom_print import custom_print

app = None
app = Flask(__name__)

animal_list = [Cat('Sushy'), Dog('Fido'), Tiger('Incineroar')]

print_temp = print
print = custom_print.print
print("Yeah")
print = print_temp


@app.route("/")
def root():
    #print("Hello")
    #print_temp = print
    #print = custom_print.print

    custom_print.reset()

    test_simple_loop()
    test_a_comprehensive_list_digging()
    test_a_comprehensive_list_with_condition()
    test_a_map_1()
    test_a_map_2()
    test_a_generator()

    html = 'aaaaaa' # custom_print.dump()

    #print = print_temp

    return html


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
    print(reduce((lambda x, y: x+", {}".format(y)), [animal.name for animal in animal_list]))


@print_line
def test_a_generator():
    for animal in an_animal_generator():
        print("{} (from a generator)".format(animal))


def an_animal_generator():
    for animal in animal_list:
        yield animal


#print_temp = print
#print = custom_print.print

#final_text = root()

#print = print_temp
#print(final_text)