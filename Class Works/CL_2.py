'''
ЗАДАНИЕ №1
Напишіть програму years.py, яка створить файл next_generation.txt -DONE
та запише в нього числа від 2000 до 2042 через пробіл -DONE
з переносом на новий рядок після кожного десятка (2010, 2020,...).
'''

with open('next_generation.txt', 'wt') as f:
    for year in range(2000, 2043):
        if year % 10 == 0 and year != 2000:
            f.write('\n')
        f.write(f'{year} ')

'''
ЗАДАНИЕ №2
Напишіть функцію files_copy(file_name: str, destination_file_name: str) -> bool. 
Функція приймає два параметри назву існуючого файлу та назву файлу в який буде скопійовано вміст файлу. 
Функція повертає True в разі якщо все пройшло успішно, в разі будь-якої помилки False.
'''


def files_copy(file_name: str, destination_file_name: str) -> bool:
    try:
        with open(file_name, 'rt') as f:
            text = f.read()
        with open(destination_file_name, 'wt') as f:
            f.write(text)
        return True
    except:
        return False


print(files_copy('next_generation.txt', 'new_generation'))
