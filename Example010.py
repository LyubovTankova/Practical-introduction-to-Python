# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list1 = input().split()
list2 = []
for start in range(0, (len(list1) - 1) // 2 + 1):
    list2.append(int(list1[start]) * int(list1[len(list1) - start - 1]))
print(f"Произведение пар чисел списка - {list2}")