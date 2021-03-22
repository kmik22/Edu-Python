import json
import pickle

'''
Напишіть програму shoppping_deserializer.py. 
Візьміть дані з файлів з серіалізованими динними з попереднього завдання та десеріалізуйте їх та виведіть на екран.
'''
with open("shopping_list.pkl", 'rb') as f:
    loaded_pickle = pickle.load(f)
print(loaded_pickle)

with open("shopping_list.json", 'r') as f:
    loaded_json = json.load(f)
print(loaded_json)