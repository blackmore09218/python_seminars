'''задача 4 НЕГА необязательная Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
*Пример:*
- для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]'''

k = int(input('Введите натуральное число больше 1:   '))
array = list()
array.append(0)
array.append(1)
for i in range(2, k+1):
    array.append(array[i-1]+array[i-2])
reverse_array = array[1:]
for i in range(1, k, 2):
    reverse_array[i]*= -1
reverse_array = reverse_array[::-1]
print(reverse_array + array)