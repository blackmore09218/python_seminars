#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается 
# сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('Введите количество рядов в шоколадке - n:   '))
m = int(input('Введите количество столбцов в шоколадке - m:   '))
k = int(input('Введите требуемое количество долек - k:   '))
if (k%n==0 or k%m==0) and k<m*n:
    print('Можно!!!')
else:
    print('Нельзя!!!')