# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра. (Например: Треугольник дз1, дроби дз2)
# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. 
def reduc(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n

class Fractions:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
       
    def __add__(self, other):
        new_num = self.numerator * other.denominator + self.denominator * other.numerator
        new_den = self.denominator * other.denominator
        reduction = reduc(new_num, new_den)
        print("Сумма", new_num//reduction, "/" ,new_den//reduction)    
        return Fractions(new_num, new_den)

    def __prod__(self, other):
        prod_num = self.numerator * other.numerator
        prod_den = self.denominator * other.denominator
        reduction = reduc(prod_num, prod_den)
        print("Произведение", prod_num//reduction, "/" ,prod_den//reduction)
        return Fractions(prod_num, prod_den)
                  
   
r1 = Fractions(5, 8)
r2 = Fractions(7, 4)
r1.__add__(r2)
r1.__prod__(r2)