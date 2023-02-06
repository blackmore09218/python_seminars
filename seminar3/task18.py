'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N
 – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
'''
from math import ceil
N = int(input('Введите максимальный элемент в последовательности:   '))
array = [i for i in range(1,N+1)]
X = float(input('Введите число X:   '))
if X < 1:
    element = 1
elif X > N:
    element = N
else:
    left = abs(int(X)-X)
    right = abs(ceil(X)-X)
    if left == right == 0:
        element = int(X)
    elif left > right:
        element = ceil(X)
    elif left < right:
        element = int(X)
    else:
        element = [int(X), ceil(X)]
print(f'Самый близкий по значению элемент к числу X - {element}')