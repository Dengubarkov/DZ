from random import choice
import json


def id_gen():
    try:
        data = json.load(open('person.json'))
        id = len(data) + 1

    except FileNotFoundError:
        id = 1
    return "ID_" + str(id)


def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)
    person = {
        id_gen():
            {'name': name, 'tel': tel}}
    return person


def write_json(person_dict):
    try:
        data = json.load(open('person.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('person.json', 'w') as y:
        json.dump(data, y, indent=2)


persons = []
for i in range(10):
    write_json(gen_person())
