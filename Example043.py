# Создайте класс студента.Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв. 

class Verification_Name:
    def __set_name__(self, owner, name):
        self.param_name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        if not value.isalpha() or not value.istitle():
            raise Exception("На ввод ФИО допустимы данные только с первой заглавной буквы")
        instance.__dict__[self.param_name] = value


class Student:
    last_name = Verification_Name()
    first_name = Verification_Name()
    patronymic = Verification_Name()

    def __init__(self, last_name: str, first_name: str, patronymic: str):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic

    def __repr__(self):
        return f'Student({self.last_name}, {self.first_name}, {self.patronymic})' 
        
    def __str__(self):
        return f'{self.last_name} {self.first_name} {self.patronymic}'

        
s1 = Student('петрова', 'Марина', 'Олеговна')

print(s1)