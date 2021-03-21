# HOMEWORK 6
print('\nExercise_1')
def bubble_sort(myList):
    swapped = True
    ogr = len(myList) - 1
    while swapped:
        swapped = False
        for i in range(ogr):
            if myList[i] > myList[i + 1]:
                swapped = True
                myList[i], myList[i + 1] = myList[i + 1], myList[i]
        ogr -= 1
def sort_23_13(lst):
    ser = sum(lst) / len(lst)
    if ser > 0:
        last_index = len(lst) * 2 // 3
    else:
        last_index = - (len(lst) * 2 // 3)
    left_part = lst[:last_index]
    bubble_sort(left_part)
    right_part = lst[last_index:]
    right_part.reverse()
    return left_part + right_part
print(sort_23_13([1, 2, 3, 4, -5, -6, -7]))
print('\nExercise_2')
def parallel_sort(main_list, sub_list):
    swapped = True
    ogr = len(main_list) - 1
    while swapped:
        swapped = False
        for i in range(ogr):
            if main_list[i] > main_list[i + 1]:
                swapped = True
                main_list[i], main_list[i + 1] = main_list[i + 1], main_list[i]
                sub_list[i], sub_list[i + 1] = sub_list[i + 1], sub_list[i]
        ogr -= 1
def point1(ids, phones):
    parallel_sort(ids, phones)
def point2(ids, phones):
    parallel_sort(phones, ids)
def point3(ids, phones):
    print('\nДанные:')
    for id, phone in zip(ids, phones):
        print(f"{id} - {phone}")
def main_menu(ids, phones):
    while True:
        text = '--= Главное меню =--\n' \
               '1 - Отсортировать по идентификационным кодам\n' \
               '2 - Отсортировать по номерам телефона\n' \
               '3 - Вывести список пользователей с кодами и телефонами\n' \
               '4 - Выход'
        print(text)
        choice = input('Ваш выбор: ')
        if choice == '1':
            point1(ids, phones)
        elif choice == '2':
            point2(ids, phones)
        elif choice == '3':
            point3(ids, phones)
        elif choice == '4':
            break
        else:
            pass
        print('')
def main():
    ids = [8, 5, 1, 2, 6, 4, 3, 7]
    phones = [121452, 124534, 153364, 532463, 143524, 542124, 423542, 912435]
    main_menu(ids, phones)
main()
print('\nExercise_3')
lst1 = (1, 2, 3, 4)
lst2 = (3, 4, 5, 9)
lst3 = (5, 6, 7, 8)
def unnums(lstmain,complst1, complst2):
    uniq = []
    for num in lstmain:
        isuniq = True
        for el in complst1 + complst2:
            if num == el:
                isuniq = False
                break
        if isuniq == True:
            uniq.append(num)
    return uniq
print('Lst1 unique nums:', *unnums(lst1, lst2, lst3))
print('Lst2 unique nums:', *unnums(lst2, lst1, lst3))
print('Lst3 unique nums:', *unnums(lst3, lst2, lst1))
print('\nExercise_4')
lst1 = (2, 2, 6, 8, 10, 11, 11, 11, 22)
lst2 = (1, 2, 7, 9, 100, 13, 11, 13, 22)
lst3 = (3, 2, 7, 6, 10, 11, 11, 14, 22)
def match(lst1, lst2, lst3):
    mlist = []
    for i in range(len(lst1)):
        if lst1[i] == lst2[i] == lst3[i]:
            # print(lst1[i], end=" ")
            mlist.append(lst1[i])
    return mlist
print(match(lst1, lst2, lst3))
