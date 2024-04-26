# Создайте список из случайных чисел.Найдите количество различных элементов в нем.

import random
n = [random.randint(1, 10) for _ in range(7)]
print('Список: ', n)
count = 0
lst = []
for el in n:
    if el not in lst:
        count += 1
        lst.append(el)
print(len(lst))