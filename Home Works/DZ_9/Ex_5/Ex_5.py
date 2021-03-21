"""
EX5: Дан текстовый файл. Посчитать сколько раз в нем встречается заданное пользователем слово.
"""

file = open('Text.txt')
text = file.read()
file.close()

textN = text.lower().split()
keyW = input('Введите слово: ').lower()
countW = 0

for word in textN:
    if keyW == word.strip('-=.,!?:{}"\/|'):
        countW +=1
print(countW)