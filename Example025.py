# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# a, b = input("1 строка вида “a/b”: "), input("2 строка вида “a/b”: ")
# f1, f2 = F(a), F(b)
# print(f"{a} + {b} = {f1 + f2}")
# print(f"{a} * {b} = {f1 * f2}")
from fractions import Fraction as F

def fractions(a, b):
    numerator_a, denominator_a = map(int, a.split("/"))
    numerator_b, denominator_b = map(int, b.split("/"))

    sum_numerator = numerator_a * denominator_b + numerator_b * denominator_a
    sum_denominator = denominator_a * denominator_b
    sum_fractions = (sum_numerator, sum_denominator)

    prod_numerator = numerator_a * numerator_b
    prod_denominator = denominator_a * denominator_b
    prod_fractions = (prod_numerator, prod_denominator)

    return sum_fractions, prod_fractions

a = "5/10"
b = "10/5"

sum_fractions, prod_fractions = fractions(a, b)
f1, f2 = F(a), F(b)

print(f"{a} + {b} = {f1 + f2}")
print(f"{a} * {b} = {f1 - f2}")