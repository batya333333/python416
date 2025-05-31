from random import *
import json


def get_person():
    name = ''
    tel = ''
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)
    print(name)

    while len(tel) != 5:
        tel += choice(nums)
    print(tel)

    person = {
        'name': name,
        'tel': tel
    }
    return person, tel


# print(get_person())


def write_json(person_dict,num):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = dict()

    data[num] = person_dict

    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(get_person()[0],get_person()[1])
