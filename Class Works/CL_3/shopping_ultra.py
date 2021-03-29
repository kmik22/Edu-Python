import json

'''
EX_3
Напишіть програму shopping_ultra.py, що буде надавати можливість
додавати нові списки, видаляти вже існуючі, знаходити найдорожчий і найдешевший список з покупками,
зчитувати дані при першому вході з файлу (де дані серіалізовані)
та після завершення роботи серіалізувати та зберігати у файл (формат серіалізації json).
'''

SHOP_LIST = []


# def add_list(your_list: dict):
#     with open('SHOP_LIST_EX3', 'w') as f:
#         f.write(json.dumps(your_list, indent=4))

def add_list(your_list: dict):
    SHOP_LIST.append(your_list)


add_list({
    'Potato': 10,
    'Tomato': 15,
    'Onion': 13,
    'Pickle': 22
})

add_list({'Oil': 6,
          'Seaweed': 4,
          'Candy': 10,
          'Tea': 11
          })

print(SHOP_LIST)


def del_list(list_num: int):
    del SHOP_LIST[list_num]


del_list(1)

print(SHOP_LIST)

def most_exp():
