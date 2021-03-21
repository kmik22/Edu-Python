"""
EX4: Дан текстовый файл. Найти длину самой длинной строки.
"""

file = open('Text.txt')
linelist = file.readlines()
file.close()

longest = linelist[0]
for line in linelist:
    if len(line) > len(longest):
        longest = line
print(longest)
