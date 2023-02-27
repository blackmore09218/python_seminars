import json

def print_menu():
    print('''
0 - выход из справочника
1 - показать весь справочник
2 - добавить запись
3 - удалить запись
4 - редактировать запись в справочнике
5 - поиск по введенным параметрам ''')

def load_spravochnik():
    f_name='BD.json'
    with open(f_name, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
        print('БД успещно загружена: \n')
    for item in BD_local:
        print (item)
    print()

def add_item():
    new_item = {}
    new_item['ФИО'] = input('Введите фамилию, имя и отчество через пробел:   ')

    new_item['телефон(ы)'] = []
    answer = input('Есть ли у нового абонента очередной номер телефона? (1 - да, 0 - нет)   ')
    while answer != '0':
        if answer not in '01':
            answer = input('Введите корректный ответ на предыдущий вопрос (1- да, 0 - нет)   ')
        else:
            new_item['телефон(ы)'].append(input('Введите очередной номер телефона абонента:   '))
            answer = input('Есть ли у нового абонента очередной номер телефона? (1 - да, 0 - нет)   ')

    new_item['e-mail'] = []
    answer = input('Есть ли у нового абонента очередной e-mail? (1 - да, 0 - нет)   ')
    while answer != '0':
        if answer not in '01':
            answer = input('Введите корректный ответ на предыдущий вопрос (1- да, 0 - нет)   ')
        else:
            new_item['e-mail'].append(input('Введите очередной e-mail абонента:   '))
            answer = input('Есть ли у нового абонента очередной e-mail? (1 - да, 0 - нет)   ')
    
    new_item['город'] = input('Введите город:   ')
    new_item['пол'] = input('Введите пол (М - мужской, Ж - женский):   ')
    new_item['год рождения'] = input('Введите год рождения:   ')

    f_name='BD.json'
    with open(f_name, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
        BD_local.append(new_item)
    with open('BD.json', 'w', encoding='utf-8') as fw:
        fw.write(json.dumps(BD_local, ensure_ascii=False))
        print('БД успещно сохранена')

def remove_item():
    f_name='BD.json'
    with open(f_name, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
    item_to_remove = input('Введите ФИО для удаления данных из базы:   ')
    flag = False
    for i in range(len(BD_local)):
        if item_to_remove in BD_local[i]['ФИО']:
            del BD_local[i]
            flag = True
            break
    if flag == False:
        print('Такого имени нет в базе!!!')
    else:
        with open('BD.json', 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(BD_local, ensure_ascii=False))
            print('Запись успешно удалена')

def edit_item():
    item_to_edit = input('Введите имя:   ')
    f_name='BD.json'
    with open(f_name, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
    flag = False
    for i in range(len(BD_local)):
        if item_to_edit in BD_local[i]['ФИО']:
            dictionary_to_edit = BD_local[i]
            flag = True
            count = i
            break
    if flag == False:
        print('Такого имени нет в базе!!!')
    else:
        print('''
1 - редактировать ФИО
2 - редактировать телефон(ы)
3 - редактировать e-mail
4 - редактировать город
5 - редактировать пол (?!)
6 - редактировать год рождения''')
        number_to_edit = int(input('Введите номер команды для редактирования:   '))
        if number_to_edit == 1:
            dictionary_to_edit['ФИО'] = input('Введите актуальные ФИО:  ')
        elif number_to_edit == 2:
            dictionary_to_edit['телефон(ы)'] = input('Введите актуальные номера телефонов через пробел:   ').split()
        elif number_to_edit == 3:
            dictionary_to_edit['e-mail'] = input('Введите актуальные e-mail через пробел:   ').split()
        elif number_to_edit == 4:
            dictionary_to_edit['город'] = input('Введите актуальный город:   ')
        elif number_to_edit == 5:
            dictionary_to_edit['пол'] = input('Введите актуальный пол (М - мужской, Ж -женский):   ')
        elif number_to_edit == 6:
            dictionary_to_edit['год рождения'] = input('Введите актуальный год рождения  ')
        else:
            print('Введен неверный номер команды для редактирования')
        BD_local[count] = dictionary_to_edit
        with open('BD.json', 'w', encoding='utf-8') as fw:
            fw.write(json.dumps(BD_local, ensure_ascii=False))
            print('Запись успешно отредактирована!!!')

def search():
    search_parameter = input('Введите параметр для поиска:   ')
    f_name='BD.json'
    with open(f_name, 'r', encoding='utf-8') as fh:
        BD_local = json.load(fh)
    flag = False
    for i in range(len(BD_local)):
        if search_parameter in BD_local[i]['ФИО']:
            print(BD_local[i])
            flag = True
            continue
        for j in range(len(BD_local[i]['телефон(ы)'])):
            if search_parameter in BD_local[i]['телефон(ы)'][j]:
                print(BD_local[i])
                flag = True
                break
                continue
        for j in range(len(BD_local[i]['e-mail'])):
            if search_parameter in BD_local[i]['e-mail'][j]:
                print(BD_local[i])
                flag = True
                break
                continue
        if search_parameter in BD_local[i]['город']:
            print(BD_local[i])
            flag = True
            continue
        if search_parameter in BD_local[i]['год рождения']:
            print(BD_local[i])
            flag = True
            continue
    if flag == False:
        print('Введенного параметра нет в базе!!!')

