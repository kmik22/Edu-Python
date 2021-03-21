print('Ex_1')
"""
Задание 1
Реализуйте класс «Автомобиль».
Необходимо хранить в полях класса:
название модели, год выпуска, производителя, объем двигателя, цвет машины, цену.
Реализуйте методы класса для ввода данных, вывода данных,
реализуйте доступ к отдельным полям через методы класса (property)
"""

class Auto:
    def __init__(self, make, model, year, engine_volume, color, price):
        self.__make = make.upper()
        self.__model = model.upper()
        self.__year = year
        self.__engine_volume = engine_volume
        self.__color = color.upper()
        self.__price = price

    def __str__(self):
        return f"\nCAR FOR SALE INFORMATION:\n" \
              f"MAKE: {self.__make} \n" \
              f"MODEL: {self.__model}\n" \
              f"YEAR: {self.__year}\n" \
              f"ENGINE: {self.__engine_volume}\n" \
              f"COLOR: {self.__color}\n" \
              f"PRICE: {self.__price}\n"

    @classmethod
    def input_auto(cls):
        dict = {}
        fields = ['make', 'model', 'year', 'engine', 'color', 'price']
        types = [str, str, int, float, str, int]

        for field, converter in zip(fields, types):
            dict[field] = converter(input(f'{field.upper()}: '))

        return cls(*dict.values())

    def print(self):
        print(self)

    @property
    def make(self):
        return self.__make

    @property
    def color(self):
        return self.__color.upper()

    @color.setter
    def color(self, value):
        self.__color = value.upper()

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value


auto1 = Auto('bmw', 'x4', 2020, 3.0, 'white', 65_000)
auto2 = Auto.input_auto()

print('Ex_2')
"""
Реализуйте класс «Книга». Необходимо хранить в полях класса: 
название книги, год выпуска, издателя, жанр, автора, цену. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса. 
Реализуйте хранение атрибута каталожный номер (как порядковый номер созданного объекта) 
"""



print('Ex_3')
"""
Реализуйте класс «Стадион». Необходимо хранить в полях класса: 
название стадиона, дату открытия, страну, город, вместимость. 
Реализуйте методы класса для ввода данных, вывода данных, 
реализуйте доступ к отдельным полям через методы класса"""