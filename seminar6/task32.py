'''Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше 
заданного максимума)'''

from random import randint
amount = int(input('Введите количество элементов массива:   '))
array = [randint(-100,100) for _ in range(amount)]
bottom = int(input('Введите нижнюю границу интервала:   '))
top = int(input('Введите верхнюю границу интервала:   '))
print(array)
index_list = []
for i in range(amount):
    if bottom <= array[i] <= top:
        index_list.append(str(i))
print(f'Индексы элементов массива (списка), значения которых принадлежат заданному диапазону: {", ".join(index_list)}')