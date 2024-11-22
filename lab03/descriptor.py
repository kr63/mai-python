import re


class Integer:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")

        self.value = value


class String:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):
        if not isinstance(value, str):
            raise TypeError("Must be a string")

        if not re.match(r'(^[A-Z]+[a-z].*$)', value):
            raise TypeError("Must start with capital letter and contain only letters")

        self.value = value


class PositiveInteger:
    def __get__(self, obj):
        return self.value

    def __set__(self, obj, value):

        if not isinstance(value, int):
            raise TypeError("Must be an integer")

        if value < 0:
            raise TypeError("Must be a positive integer")

        self.value = value


class Data:
    num = Integer()
    name = String()
    price = PositiveInteger()

    def __init__(self, num, name, price):
        self.num = num
        self.name = name
        self.price = price
