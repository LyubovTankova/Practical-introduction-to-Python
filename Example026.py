# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата. 

def hex_func (number: int, n = 16):
    hex_number = "0123456789abcdef"
    result_str = ""
    while number > 0:
        result_str = hex_number[number % n] + result_str
        number = number // n
    return result_str
    
number = 123
print(hex_func(number))
print(hex(number))