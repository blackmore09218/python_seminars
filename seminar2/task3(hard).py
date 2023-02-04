'''Задача 3 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (Теорема Де Моргана) .
 Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные, проверяем это утверждение 100 раз,
  с помощью модуля time выводим на экран , сколько времени отработала программа. В конце вывести результат проверки истинности этого утверждения.'''

from random import randint, choice
from time import process_time
total_bool_var = True
for i in range(101):
    number_of_predicates = randint(5,25)
    value_list = list()
    for j in range(number_of_predicates):
        value_list.append(choice([True,False]))
    left_bool_var = False
    for j in range(number_of_predicates):
        left_bool_var = left_bool_var or value_list[j]
    left_bool_var = not left_bool_var
    right_bool_var = True
    for j in range(number_of_predicates):
        value_list[j] = not value_list[j]
        right_bool_var = right_bool_var and value_list[j]
    total_bool_var = total_bool_var and (left_bool_var == right_bool_var)
print(total_bool_var)
print('Время, затраченное на выполнение программы:    ', process_time(), 'секунд')

   
    
