# Exercise 1
print()
my_num = int(input('Four digit #: '))

a = my_num // 1000
b = my_num % 1000 // 100
c = my_num % 100 // 10
d = my_num % 10

print()

print(a)
print(b)
print(c)
print(d)

if a < b:
    a = b
if a < c:
    a = c
if a < d:
    a = d

print(a, 'is the biggest digit')

print()

# Exercise 2
wage = int(input('Your monthly wage: '))
inter = int(input('Your monthly interest expense: '))
util = int(input('Your utilities expense: '))

print('\n\tYOU HAVE', wage - inter - util, 'UAH LEFT AFTER ALL EXPENSES.')
print()

# Exercise 3
e = "«Life is what happens\n\t\t\t when you're busy\n\t\t\t\t\t\t making other plans»\n\t\t\t\t\t\t\t\t John Lennon."
print(e)











