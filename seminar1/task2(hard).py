from decimal import Decimal
number = Decimal(input('Введите положительное вещественное число c мантиссой не более 27 десятичных знаков:\n'))
int_number = int(number)
while int_number == 0:
    number*=10
    int_number = int(number)
count = 0
while int_number != 0:
    int_number //= 10
    count+=1
number = number * (10**(27-count))
summa = 0
while number != 0:
    summa += number % 10
    number //= 10
print('Сумма цифр введенного числа равна:  ', int(summa))
