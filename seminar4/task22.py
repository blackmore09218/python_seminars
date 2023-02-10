'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.'''

from random import randint
n = int(input('Введите n:   '))
m = int(input('Введите m:   '))
array_n = []
for i in range(n):
    array_n.append(randint(-100, 100))
print(array_n)
array_m = []
for i in range(m):
    array_m.append(randint(-100, 100))
print(array_m)
result_array = []
for i in range(n):
    for j in range(m):
        if array_n[i] == array_m[j]:
            result_array.append(array_m[j])
result_array = set(result_array)
result_array = list(result_array)
result_array.sort()
print('Числа, присутствующие в обоих массивах:   ', result_array)