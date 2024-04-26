# Еще немного о друзьях
# Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
# Выведите средний возраст всех друзей и самое длинное имя.


N = int(input('Количество друзей:'))
friends = []
age = 0
for i in range(N):
    name = input('Имя и возраст друга через пробел:').split()
    friends.append(name[0])
    age = age + int(name[1])
age = age / N
print(age)
print(max(friends, key=len))