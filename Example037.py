# Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь, 
# если вызывается функция с агрументами, которые уже записаны в кэше - вернуть результат из кэша, 
# если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.
import json
from typing import Callable


def json_logging(func: Callable):
    try:
        with open(f'{func.__name__}.json', 'r') as data:
            result_list = json.load(data)
    except FileNotFoundError:
         result_list = [] 

    cache = {}
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if args in cache:
            print('из кэша')
            return cache[args]     
        else:
            print('вычисляю')
            cache[args] = result
            result_list.append({'args': args,
                                'result': result})
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result_list, data, indent=4)
        return result
    return wrapper 
   
    
@json_logging
def sum_args(*args, **kwargs):
    return sum(args)


if __name__ == "__main__":
    print(sum_args(5, 5))
    print(sum_args(5, 5, 5))
    print(sum_args(5, 5))
    print(sum_args(5, 5, 5, 5))
    print(sum_args(5, 5))
    print(sum_args(5, 5, 5, 5))