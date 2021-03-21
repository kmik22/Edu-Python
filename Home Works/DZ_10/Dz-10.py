'''
Реализуйте функцию которая будет
принимать в качестве аргумента словарь
и записывать его в файл в сериализованном виде
'''

import json


def ser_dict(dict):
    file = open("Dict.json", 'wt')
    file.write(json.dumps(dict, indent=4))
    file.close()

animals = [
    {
        'type': 'rabbit',
        'name': 'Katia',
        'm': 2
    },
    {
        'type': 'lion',
        'name': 'Grisha',
        'm': 21,
        'is_alive': True
    },
]

ser_dict(animals)
