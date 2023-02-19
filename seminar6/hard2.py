'''задача 2 HARD необязательная
Сгенерировать массив случайных целых чисел размерностью m*n (размерность вводим с клавиатуры) , причем чтоб количество элементов было четное. 
Вывести на экран красивенько таблицей. Перемешать случайным образом элементы массива, причем чтобы каждый гарантированно и только один раз переместился 
на другое место и выполнить это за m*n / 2 итераций. То есть если массив три на четыре, то надо выполнить не более 6 итераций. И далее в конце опять 
вывести на экран как таблицу.'''

from random import randint, choice
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

rows = int(input('Введите количество строк массива (четное) :   '))
columns = int(input('Введите количество столбцов массива:   '))
array = init_array(rows*columns)
print_array(array)
print()

index_list = list(range(rows*columns))
for i in range(int(len(array)/2)):
    ind_1 = choice(index_list)
    del index_list[index_list.index(ind_1)]
    ind_2 = choice(index_list)
    del index_list[index_list.index(ind_2)]
    middle = array[ind_1]
    array[ind_1] = array[ind_2]
    array[ind_2] = middle
print_array(array)
