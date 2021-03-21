"""
Дан текстовый файл. Удалить из него последнюю строку.
Результат записать в другой файл.
"""

file = open('Text.txt')
text = file.readlines()
file.close()
text1 = text[:-1]
text2 = ''.join(text1)
print(text2)

fileN = open("NewText.txt", "wt")
fileN.writelines(text2)
fileN.close()

