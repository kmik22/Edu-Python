import yaml

dict_exam = {
    "a": "Hey,",
    1: True,
    22: "Kyle",
    'b': "WORLD!"
}

print(yaml.dump(dict_exam))