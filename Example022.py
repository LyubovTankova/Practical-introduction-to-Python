# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def RLE_Coding(string):
    res = ''
    count = 1
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            count += 1
        else:
            res = res + str(count) + string[i]
            count = 1
    if count > 1 or (string[len(string)-2] != string[-1]):
        res = res + str(count) + string[-1]
    return res


def RLE_Decoding(text):
    num = ''
    res = ''
    for i in range(len(text)):
        if text[i].isdigit():
            num += text[i]
        else:
            res = res + text[i] * int(num)
            num = ''
    return res


a = input("Введите текст: ")
print(f"Сжатие: {RLE_Coding(a)}")
print(f"Восстановление данных: {RLE_Decoding(RLE_Coding(a))}")