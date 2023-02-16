'''Задача HARD SORT необязательная.
Задайте двумерный массив из целых чисел. Количество строк и столбцов задается с клавиатуры. Отсортировать элементы по возрастанию слева направо и сверху вниз.

Например, задан массив:
1 4 7 2
5 9 10 3

После сортировки
1 2 3 4
5 7 9 10'''

from random import randint
def init_array(number_of_elements):
    arr = []
    for i in range(number_of_elements):
        arr.append(randint(100,999))
    return arr
          
def print_array(arr):
    for i in range(rows):
        for j in range(columns):
            print(arr[i*columns+j], end=' ')
        print()

rows = int(input('Введите количество строк массива:   '))
columns = int(input('Введите количество столбцов массива:   '))
array = init_array(rows*columns)
print_array(array)
print()
array.sort()
print('Отсортированный массив: \n')
print_array(array)