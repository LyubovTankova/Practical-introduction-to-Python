# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = input("Введите текст: ")
print(f"Ваш текст: {text}")
new_text = 'абв'
lst = [i for i in text.split() if new_text not in i]
print(f'Итог: {" ".join(lst)}')