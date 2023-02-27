import json
from functions import *
print_menu()
number_of_command = int(input('Выберите команду меню:    '))
while True:
    if number_of_command == 0:
        print()
        print('До свидания!!!')
        break
    elif number_of_command == 1:
        load_spravochnik()
        print_menu()
        number_of_command = int(input('Выберите команду меню:    '))
    elif number_of_command == 2:
        add_item()
        print_menu()
        number_of_command = int(input('Выберите команду меню:    '))
    elif number_of_command == 3:
        remove_item()
        print_menu()
        number_of_command = int(input('Выберите команду меню:    '))
    elif number_of_command == 4:
        edit_item()
        print_menu()
        number_of_command = int(input('Выберите команду меню:    '))
    elif number_of_command == 5:
        search()
        print_menu()
        number_of_command = int(input('Выберите команду меню:    '))