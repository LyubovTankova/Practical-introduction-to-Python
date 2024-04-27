# Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. 
# Превратите функции в методы класса, а параметры в свойства.
# Задания должны решаться через вызов методов экземпляра. (Например: Треугольник дз1, дроби дз2)
# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
# Дано a, b, c - стороны предполагаемого треугольника. 
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
# Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
# то треугольника с такими сторонами не существует. 
# Отдельно сообщить является ли треугольник разносторонним, 
# равнобедренным или равносторонним.

class Treagle:
    def __init__(self, A: int, B: int, C: int) -> None:
        self.A = A
        self.B = B
        self.C = C
        
    def compare(self):
        if (self.A + self.B < self.C or self.A + self.C < self.B or self.B + self.C < self.A):
            return 'Треугольника c такими сторонами не существует!'
        else:
            return 'Треугольник существует'
             
    def form_treagle(self):
        if (self.A == self.B and self.B == self.C and self.C == self.A):
           return 'Треугольник равносторонний.'
        elif (self.A != self.B and self.B != self.C):
           return 'Треугольник разносторонний.'  
        else:
           return 'Треугольник равнобедренный.'  


r1 = Treagle(4, 4, 4)
r2 = Treagle(4, 5, 6)
r3 = Treagle(4, 4, 8)
r4 = Treagle(4, 4, 12)
print(r1.compare(), r1.form_treagle())
print(r2.compare(), r2.form_treagle())
print(r3.compare(), r3.form_treagle())
print(r4.compare())