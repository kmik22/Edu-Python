# HOMEWORK 5-6
print('\nExercise_1')
def exercise1(a):
    print('''\t"Don't compare yourself with anyone in this world...if you do so, you are insulting yourself."\n\tBill Gates''' + a)
    return exercise1
exercise1('.')
print('\nExercise_2')
def nums(a, b):
    for i in range(a + 1 , b):
        if i % 2 == 0:
            print(i, end=" ")
    return nums
nums(2, 22)
print('\n\nExercise_3')
def prime(a, b):
    count = 0
    for num in range(a, b + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                count += 1
                # print(num, end=" ")
    return count
quant = prime(1, 21)
print("Q-ty of prime nums:", quant)
print('\nExercise_4')
def small(a, b, c, d, e):
    mylist = [a, b, c, d, e]
    smalest =  mylist[0]
    for num in mylist:
        if num < smalest:
            smalest = num
            print("Smallest #:", smalest)
    return small
small(1, 21, -1, 4,100)
print('\nExercise_5')
def digits(num):
    mylist = [int(i) for i in str(num)]
    return print(len(mylist))
digits(123456789)
print('\nExercise_6')
def digits(num):
    mylist = [int(i) for i in str(num)]
    print(mylist == mylist[::-1])
    return digits
digits(12344321)
print('\nExercise_7')
def isprime(number):
    if number < 2:
        return False
    for num in range(2, number//2 + 1):
        if number % num == 0:
            return False
    return True
def primeN(n):
    count = 0
    a = 0
    while True:
        if isprime(a):
            count += 1
            if count == n:
                return a
        a += 1
print(primeN(5))
print('\nExercise_8')
def lis2deg(listnum, degree):
    return [num ** degree for num in listnum]
print(lis2deg([1,2,3,4,5],2))
print('\nExercise_9')
def _euclid(big, small):
    ost = big % small
    if ost == 0:
        return small
    else:
        return _euclid(small, ost)
def euclid(n1, n2):
    if n1 > n2:
        big = n1
        small = n2
    else:
        small = n1
        big = n2
    return _euclid(big, small)
print(euclid(18,30))
print('\nExercise_10')
import time
import random
def optime(func):
    def newfunc(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        timediff = t2 - t1
        print(round(timediff * 1000, 2))
        return result
    return newfunc
@optime
def genlist(a, b, n=100):
    lis1 = [random.randint(a, b) for _ in range(n)]
    return lis1
genlist(1, 100, 1000)

