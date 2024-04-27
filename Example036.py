# Напишите функцию, которая сериализует содержимое текущей директории в json-файл. 
# В файле должен храниться список словарей, словарь описывает элемент внутри директории: 
# имя, расширение, тип. Если элемент - директория, то только тип и имя. 
# Пример результата для папки, где лежит файл test.txt и директория directory_test:
# [
# {
# 'name': 'test',
# 'extension': '.txt',
# 'type': 'file'
# },
# {
# 'name': 'directory_test',
# 'type': 'directory',
# }
# ]
import os
import json
import sys


def directory_structure(path):
    structure = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        structure['type'] = 'directory'
        structure['attachment'] = [directory_structure(os.path.join(path,f)) for f in os.listdir\
(path)]       
    else:
        structure['extension'] = os.path.splitext(path)[1]
        structure['type'] = "file"  
    return structure  
 
if __name__ == '__main__':
    try:
        directory = sys.argv[1]
    except IndexError:
        directory = os.getcwd()

with open('json_file.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(directory_structure(directory), indent=4, sort_keys=False,))
f.close()