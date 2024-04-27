# Создайте класс Матрица. Добавьте методы для: вывода на печать, сравнения, сложения

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.matrix])
    
    def __repr__(self):
        return f'Matrix({self.matrix})'  

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __add__(self, other):
        res = [[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))]
                for i in range(len(self.matrix))]
        if len(self.matrix[0]) != len(other.matrix[0]):
            raise Exception('Разные размеры матрицы')
        return Matrix(res)
  

r1 = Matrix([[5, 5, 1], [8, 7, 3]])
r2 = Matrix([[3, 9, 2], [4, 0, 5]])

print(repr(r1), repr(r2), sep='\n')
print(r1.__eq__(r2))
print(r1.__add__(r2))