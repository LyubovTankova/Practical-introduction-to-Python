# Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. 
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Ввод: c:/Users/Vladislav/Desktop/deep_to_python/test.txt
# Вывод: ( 'c:/Users/Vladislav/Desktop/deep_to_python/', 'test', '.txt')
import os

string =  "d:\Task\Python\Introducing Python\Examples Python\Example031.py"

def function_path(path):
    path_file, extension_file = os.path.splitext(path)
    name, file_name = os.path.split(path_file)
    return name, file_name, extension_file

print(f'Абсолютный путь до файла {string}')
print(f'Кортеж: Путь, имя файла, расширение файла: {function_path(string)}')