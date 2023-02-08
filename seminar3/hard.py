'''Задача HARD необязательная Имеется список чисел. Создайте список, в который попадают числа, описывающие максимальную возрастающую 
последовательность. Порядок элементов менять нельзя. Одно число - это не последовательность. Пример:
[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7]
[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5]
[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5]'''

from random import randint
num_array = [randint(1,100) for i in range(101)]
print(num_array)
num_array.sort()
num_array = set(num_array)
num_array = list(num_array)
count = 1
tuple_array = list()
for i in range(len(num_array)-1):
    if num_array[i+1] - num_array[i] == 1:
        count+=1
    else:
        if count > 1:
            tuple_array.append(i)
            tuple_array.append(count)
            count = 1
max_length = tuple_array[1]
for i in range (3, len(tuple_array)-1, 2):
    if tuple_array[i] > max_length:
        max_length = tuple_array[i]
for i in range (1, len(tuple_array)-1, 2):
    if tuple_array[i] == max_length:
        print('Числа, описывающие максимальную возрастающую последовательность:   ', [tuple_array[i-1]-tuple_array[i]+1, tuple_array[i-1]+1])
