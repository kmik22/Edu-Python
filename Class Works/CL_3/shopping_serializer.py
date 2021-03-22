import pickle
import json

'''
Напишіть програму shopping_serializer.py.
Створіть набір покупок, у вигляді списку словників з набором продуктів та їх вартістю.
Дані серіалізуйте за допомогою pickle у файл shopping_list.pkl
та за допомогою json у файл shopping_list.json.
'''

purchases = [{
    'Potato': 10,
    'Tomato': 15,
    'Onion': 13,
    'Pickle': 22
},
    {'Oil': 6,
    'Seaweed': 4,
    'Candy': 10,
    'Tea': 11
     }]

with open('shopping_list.pkl', 'wb') as f:
    f.write(pickle.dumps(purchases))

with open('shopping_list.json', 'w') as f:
    f.write(json.dumps(purchases, indent=4))
