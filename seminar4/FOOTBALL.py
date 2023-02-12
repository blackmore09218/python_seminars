'''Задача FOOTBALL необязательная. Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча и выводит 
на стандартный вывод сводную таблицу результатов всех матчей.За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.
Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр. После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой
Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков
Конкретный пример ввода-вывода приведён ниже. Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6'''

def games_wins_draws_loses_points(team):
    games = 0
    for i in common_list:
        if i == team:
            games+=1
    count = 0
    wins = 0
    draws = 0
    loses = 0
    for i in range(0, len(common_list), 2):
        if common_list[i] == team and i%4==0:
            if int(common_list[i+1]) > int(common_list[i+3]):
                wins+=1
            elif int(common_list[i+1]) == int(common_list[i+3]):
                draws+=1
            else:
                loses+=1
        if common_list[i] == team and i%4==2:
            if int(common_list[i+1]) > int(common_list[i-1]):
                wins+=1
            elif int(common_list[i+1]) == int(common_list[i-1]):
                draws+=1
            else:
                loses+=1
    points = 3*wins + draws
    result =str(games) + ' ' + str(wins) + ' ' + str(draws) + ' ' + str(loses) + ' ' + str(points)
    return result

n = int(input('Введите количество завершенных игр:   '))
count = 1
common_list = []
while count <= n:
    common_list.extend(input(f'Введите результат {count} игры:  ').split(';'))
    count+=1
teams_list = []
for i in range(len(common_list)):
    if common_list[i].isdigit() == False and common_list[i] not in teams_list:
        teams_list.append(common_list[i])
for i in range(len(teams_list)):
    print(f'{teams_list[i]}: {games_wins_draws_loses_points(teams_list[i])}')
