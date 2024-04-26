# Старший и младший.
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Найдите самого младшего из друзей и выведите его имя.

N = int(input("Количество друзей: "))
friends = {}
for i in range(N):
    name = input("Имя - ")
    age = int(input("Возраст - "))
    friends[name] = age
min_age = min(friends.values())
for name, person in friends.items():
    if person == min_age:
        print(name)