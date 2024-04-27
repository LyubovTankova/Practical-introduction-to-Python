# 1. Напишите функцию для транспонирования матрицы 
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
import numpy as numpy

## matrix = numpy.arange(6).reshape((2, 3))
matrix = [[1, 2, 3], [4, 5, 6]]
print("Origin matrix")
print(matrix)

transponse_matrix = numpy.transpose(matrix)
print('Transponsed matrix')
print(transponse_matrix)