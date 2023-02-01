from view import creating
from download import writing

def greeting():
    print("Телефонный справочник!")
def collect ():
    info = []
    Last_Name = input('Введите фамилию: ')
    info.append(Last_Name)
    Name = input('Введите имя: ')
    info.append(Name)
    phone_number = input('Укажите телефон: ')
    info.append(phone_number)
    Comment = input('Укажите комментарий: ')
    info.append(Comment)
    return [Last_Name, Name, phone_number, Comment]