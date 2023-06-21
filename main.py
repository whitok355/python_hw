# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
import re

def checkName (value) :
    return re.match(r'[А-ЯЁ][а-яё]+\s+[А-ЯЁ][а-яё]+(?:\s+[А-ЯЁ][а-яё]+)?', value)

def checkPhone(value) :
    return re.match(r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', value)

def exp() :
    flagName = True
    while flagName :
        name = str(input("Введите ФИО: "))
        if checkName(name):
            flagName = False
            flagNumber = True
            while flagNumber :
                number = str(input("Введите номер телефона: "))
                if checkPhone(number) :
                    with open('./telephone directoryю.txt', 'a', encoding='utf-8') as inData :
                        inData.write(f" {name.strip()} : {number.strip()} \n")
                        flagNumber = False
                        print("Запись успешно добавлена")
                else:
                    print("Введите корректный номер телефона")
        else :
            print("Введите корректное ФИО")
   
def imp() :
    with open('./telephone directoryю.txt', 'r', encoding='utf-8') as outData :
        data = outData.read().splitlines()
        for user in data :
            print(user)

def change (param):
    flag_name = True
    flag_phone = True
    with open ('./telephone directoryю.txt', 'r', encoding='utf-8') as file:
        old_data = file.read().splitlines()
        for i in range(len(old_data)) :
            user_name = old_data[i].split(':')[0] 
            if user_name.lower().strip() == param.lower().strip():
                while flag_name:   
                    new_name = input("Введите новое ФИО ")
                    if checkName(new_name):
                        flag_name = False
                        while flag_phone :
                            new_number = input("Введите новый номер ")
                            if checkPhone(new_number) :
                                flag_phone = False
                                new_str = f"{new_name} : {new_number}"
                                old_data[i] = new_str
                                new_data = "\n".join(old_data)
                                with open('./telephone directoryю.txt', 'w', encoding='utf-8') as data:
                                    data.write(new_data)
                                    return True
                            else :
                                print("Введите корректный номер телефона")
            else :
                print("Введите кооректное значение. ФИО состоит из 3 значений, каждое значение начинается с заглавной буквы и написано кириллицей")

def delete(param):
    with open('./telephone directoryю.txt', 'r', encoding='utf-8') as read_data:
        old_data = read_data.read().splitlines()
        for i in range(len(old_data)) :
            user_name = old_data[i].split(':')[0]
            if user_name.lower().strip() == param.lower().strip():
                old_data.pop(i)
                new_data = "\n".join(old_data)
                with open('./telephone directoryю.txt', 'w', encoding='utf-8') as write_data:
                    write_data.write(new_data)
                    return True


operation = int(input("Введите желаемую операцию 1- экспорт, 2- импорт, 3 изменение, 4 -удаление "))

if operation == 1:
    exp()
elif operation == 2:
    imp()
elif operation == 3:
    flag_change = True
    while flag_change :
        name = str(input("Укажите ФИО пользователя по которму производится изменение "))
        if checkName(name) :
            if change(name):
                print("Изменения сохранены")
            else :
                print("У тебя руки из, что то тут не работает")
            flag_change = False
        else :
            print("Введите вкооректное значение. ФИО состоит из 3 значений, каждое значение начинается с заглавной буквы и написано кириллицей")
elif operation == 4 :
    flag_del = True
    while flag_del :
        name = str(input("Укажите ФИО пользователя по которму производится изменение "))
        if checkName(name) :
            if delete(name):
                print("Запись удалена")
            else :
                print("Данный пользователь не найден")
            flag_change = False
        else :
            print("Введите вкооректное значение. ФИО состоит из 3 значений, каждое значение начинается с заглавной буквы и написано кириллицей")
else :
    print("Вы ввели невалидное значение")