#Задача 2: Найдите сумму цифр трехзначного числа.

flag = False
while flag == False:
    number = input('Введите трехзначное число:\n')
    if len(number)!=3 or number.isdigit()==False:
        print ('Введите корректные данные')
    else:
        flag = True
sum = 0
number = int(number)
for i in range(3):
    sum+=number%10
    number//=10
print(f'Сумма цифр введенного трехзначного числа равна {sum}')