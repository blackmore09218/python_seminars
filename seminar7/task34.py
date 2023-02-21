'''Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод: Вывод:
пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам'''

phrazes_list = input('Введите стих Вини-Пуха:   ').split(' ')
vowel_numbers = []
for i in range(len(phrazes_list)):
    vowel_counter = 0
    for j in phrazes_list[i]:
        if j in 'уеыаоэяиюё':
            vowel_counter+=1
    vowel_numbers.append(vowel_counter)
flag = True
for i in range(len(vowel_numbers)-1):
    flag = flag and (vowel_numbers[i] == vowel_numbers[i+1])
if flag == True:
    print('Парам пам-пам')
else:
    print('Пам парам')
