# Создайте функцию, которая создаёт файлы с указанным расширением. Функция принимает следующие параметры: расширение 
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.
# Чтобы записать байты можно использовать список с числами и функцию bytes

from random import randint

def file_extension(extension: str, min_len_name: int = 6, max_len_name: int = 30, 
                   min_random_bytes: int = 256, max_random_bytes: int = 4096, files: int = 42):
    for i in range(files):
        name_file = set()
        for i in range(randint(min_len_name, max_len_name)):
            name_file.add(chr(randint(ord('a'), ord('z'))))

        name_file_bit = ''.join(name_file) + extension
        with open(name_file_bit, "bw") as file:
            file.write(bytes(randint(0, 255) 
            for i in range(randint(min_random_bytes, max_random_bytes))))

if __name__ == "__main__":
    file_extension("txt", files = 3)   