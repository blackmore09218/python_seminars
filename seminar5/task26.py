'''Задача 26: Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.'''

def degree(arg1,arg2):
    if arg2 == 0:
        return 1
    return arg1*degree(arg1,arg2-1)

A = int(input('Введите число А:   '))
B = int(input('Введите число B:   '))
print(degree(A,B))
