# Напишите функцию encrypt_caesar(msg, shift), которая кодирует сообщение шифром Цезаря и возвращает его.
# Шифр Цезаря заменяет каждую букву в тексте на букву, которая отстоит в алфавите на некоторое фиксированное число позиций.
# В функцию передается сообщение и сдвиг алфавита. Если сдвиг не указан, то пусть ваша функция кодирует сдвиг алфавита на 3 позиции:
# А→Г,А→Г, Б→Д,Б→Д, В→Е,В→Е,......Э→А,Э→А, Ю→Б,Ю→Б, Я→ВЯ→В
# Все символы, кроме русских букв должны остаться неизменными. Маленькие буквы должны превращаться в маленькие, большие — в большие.
# Напишите также функцию декодирования decrypt_caesar(msg, shift), также использующую сдвиг по умолчанию. При написании функции декодирования используйте
# вашу функцию кодирования.


def encrypt_caesar(msg, shift):
    small_letter = ''.join(map(chr, range(ord('а'), ord('я') + 1)))
    Caps = ''.join(map(chr, range(ord('А'), ord('Я') + 1)))
    shift = shift % len(small_letter)
    small_letter1 = small_letter[shift:] + small_letter[:shift]
    Caps1 = Caps[shift:] + Caps[:shift]
    offset = msg.maketrans(
        small_letter + Caps, small_letter1 + Caps1)
    return msg.translate(offset)


def decrypt_caesar(msg, shift):
    return encrypt_caesar(msg, -1 * shift)


msg = "Да здравствствует салат цезарь!"
shift = 5
encryption = encrypt_caesar(msg, shift)
decryption = decrypt_caesar(encryption, shift)
print(encryption)
print(decryption)