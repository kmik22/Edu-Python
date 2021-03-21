# Exercise 1
x = input('Enter smthg: ').lower().replace(' ','')
x = x.rstrip('.,!?:')
new_x = x[::-1]
if x == new_x:
    print('This is palindrome, dude!')
else:
    print('Go on!')
# Exercise 2
text = input('Enter your text: ')
keywords = input('Enter your key-words: ')
newtext = text.split()
text = text.lower().split()
keywords = keywords.lower().split()
for i in range(len(text)):
    for keyword in keywords:
        word = text[i]
        wordindex = word.find(keyword)
        lenth = len(keyword)
        if wordindex >= 0:
            leftpart = word[0:wordindex]
            centpart = word[wordindex:wordindex+lenth]
            rightpart = word[wordindex+lenth:]
            result = leftpart + centpart.upper() + rightpart
            newtext[i] = result
print(" ".join(newtext))
# Exercise 3
math = input('Enter your math expression (use "+-*/" as sing): ')
if '+' in math:
    a, b = math.split('+')
    print(int(a) + int(b))
elif '-' in math:
    a, b = a, b = math.split('-')
    print(int(a) - int(b))
elif '*' in math:
    a, b = math.split('*')
    print(int(a) * int(b))
elif '/' in math:
    a, b = math.split('/')
    print(int(a) / int(b))
# Exercise 4
list1 = list(input('Enter your list of integers: ').split())
list2 = list(input('Enter your list of integers: ').split())
newlist1 = list1[:] + list2[:]
newlist2 = list1[:]
for i in list2:
    if i not in list1: newlist2.append(i)
print(newlist2)
newlist3 = []
for i in list1:
    if i in list2: newlist3.append(i)
print(newlist3)
newlist4 = []
for i in newlist1:
    if i in newlist4: continue
    else: newlist4.append(i)
print(newlist4)
newlist5 = [min(list1), max(list1), min(list2), max(list2)]
print(newlist5)
# Exercise 5
SortedList = []
swapped = True
num = int(input("Quantity of numbers to be sorted: "))
for i in range(num):
    val = int(input("Enter one of your numbers: "))
    SortedList.append(val)
while swapped:
    swapped = False
    for i in range(len(SortedList) - 1):
        if SortedList[i] > SortedList[i + 1]:
            swapped = True
            SortedList[i], SortedList[i + 1] = SortedList[i + 1], SortedList[i]
print("\nSorted List:", SortedList)