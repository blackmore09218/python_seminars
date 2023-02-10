'''задача RLE необязательная. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
например декодирование'''


string_array = input('Введите сжимаемую строку:  ')
string_array.split()
print(string_array)
count = 1
compressioned_array = [string_array[0]]
for i in range(len(string_array)-1):
    if string_array[i] == string_array[i+1]:
        count+=1
    else:
        if count == 1:
            compressioned_array.append(string_array[i+1])
        else:
            compressioned_array.append(str(count))
            compressioned_array.append(string_array[i+1])
            count = 1
if compressioned_array[len(compressioned_array)-1].isdigit() == False and count > 1:
    compressioned_array.append(str(count))
print('Сжатие:  ', ''.join(compressioned_array))