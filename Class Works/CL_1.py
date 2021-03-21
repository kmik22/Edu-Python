import re


# Exercise_1
def char_freq(line: str):
    characters = {}
    for char in line:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters  # characters[] = 0


print(char_freq("Hello world!"))


# Exercise_2
def remove_char(text: str, pos: int):
    return text[:pos] + text[pos + 1:]


print(remove_char("Helo world!", 3))


# Exercise_3
def find_phone_nums(text: str):
    pattern = re.compile(r"\+38 0\d\d \d{3} \d{4} ")
    phonelist = []
    for match in pattern.findall(text):
        phonelist.append(match.rstrip())
    return phonelist


print(find_phone_nums('dasdsa +38 099 940 0393 23 dssad adsfds +3+38 099 940 0341 33'))
