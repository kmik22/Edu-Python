"""
Дано два текстовых файла. Выяснить, совпадают ли их строки.
Если нет, то вывести несовпадающую строку из каждого файла.
"""

file1 = open('Text_Files/Text1.txt')

file2 = open('Text_Files/Text2.txt')

lines1 = file1.readlines()
lines2 = file2.readlines()

for i in range(len(lines1)):
    if i == len(lines2):
        break
    if lines1[i].rstrip() != lines2[i].rstrip():
        print(lines1[i],'\n' + lines2[i])
        break

if len(lines2) != len(lines1):
    print("Unequal lines' quantity")

file1.close()
file2.close()