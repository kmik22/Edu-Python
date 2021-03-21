# HOME WORK 3
# Exercise #1
print('\nExercise #1')
x = int(input('Enter the 1st #: '))
y = int(input('Enter the 2nd #: '))
print('\nRange %7==0:')
for i in range(x, y+1):
    if i % 7 == 0:
        print(i, end=' ')
print()
# Exercise #2
print('\nExercise #2')
x = int(input('Enter the 1st #: '))
y = int(input('Enter the 2nd #: '))
print('\nRange:')
for a in range(x, y+1):
    print(a, end=' ')
print()
print('\nReversed range:')
for b in range(y, x-1, -1):
    print(b, end=' ')
print()
print('\nRange %7==0:')
for c in range(x, y+1):
    if c % 7 == 0:
        print(c, end=' ')
print()
print('\nQ-ty %5==0:')
z = 0
for d in range(x, y+1):
    if d % 5 == 0:
        z += 1
print(z)
print()
# Exercise #3
print('Exercise #3')
x = int(input('Enter # from range (1 ; 100): '))
y = int(input('Enter # from range (1 ; 100): '))
print()
for i in range(x, y + 1):
    if x < 1 or y > 100:
        print('ERROR: # out of range (1 ; 100)')
        break
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0: print('Fizz')
    elif i % 5 == 0: print('Buzz')
    else: print(i)
print()
print('Exercise #5')
x = int(input('Enter #: '))
y = int(input('Enter #: '))
print()
if x > y:
    x, y = y, x
for i in range(x, y + 1):
    if i % 2 != 0:
        print(i, end=' ')