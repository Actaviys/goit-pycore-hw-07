
'''
Команди:
        @1 - "hello" - Привітання з користувачем
        @2 - "add [ім'я]" - Створюю користувача
        -3- - "change [ім'я] [новий номер телефону]" - Зберігає новий номер телефону 'phone' для контакту 'username', що вже існує в записнику.
        @3 - "add-phone [ім'я] [номер телефону]" - переробив команду `change`
        @4 - "phone [ім'я]" - Виводить номер телефону контакту
        @5 - "all" - Виводить всі контакти з номерами телефонів
        @6 - "exit" - закрити програму
        @7 - "add-birthday [ім'я] [дата народження]" - додаю до контакту день народження
        @8 - "show-birthday [ім'я]" - показую день народження контакту
        9 - "birthdays" - повертає список користувачів, яких потрібно привітати по днях на наступному тижні
'''

from collections import UserDict


""" 
Спростив клас Record і добавив функціонал до UserDict. На мою думку так буде простіше
"""
class AddressBook(UserDict): #Клас для словника
    
    def add_record(self, data): #Метод для додавання словника до self.data
        super().update(data) #Додаю словник через super
    
    def find(self, fName): #Шукаю в словнику по імені
        return f"Find: {fName} {self.data.get(fName)}" #Повертаю результат
    
    def find_data_user(self, fdName, fdValue): #Метод для пошуку даних користувачів в UserDict 
        if self.data.get(fdName): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            userD = dict(self.data[fdName]) #Зберігаю словник користувача з UserDict якщо є співпадіння 
            return f"{fdName} - {fdValue} ->{userD[fdValue]}" #Повертаю результат пошуку 
    
    def find_birthday_users_for_week(self): #Метод пошуку користувачів на наступний тиждень
        pass

    def update_user(self, uUser, uDat=None): #Метод для оновлення даних користувача
        uDatKeys = "".join(dict(uDat).keys()) #Зберігаю ключ з вхідного словника
        if self.data.get(uUser): #Роблю перевірку на співпадіння в поточному словнику користувачів UserDict
            userD = dict(self.data[uUser]) #Зберігаю словник користувача з UserDict якщо є співпадіння    
            
            if userD.get(uDatKeys) == None: #Якщо немає спіпадінь в словнику користувача то додаю новий словник до користувача
                userD.update(uDat) #Добавляю до словника користувача <- вхідний словник
                super().update({uUser: userD}) #Оновлюю користувача в UserDict
                return print(f"'{uUser}' -> data has been updated")
            
            if userD.get(uDatKeys): #Якщо є ключ в користувача то оновлюю значення словника
                userD.update(uDat)
                super().update({uUser: userD})
                return print(f"'{uUser}' -> data has been updated")
            
        else: return print(f"User '{uUser}' -> is missing") #Якщо користувача не знайдено
    
    def delete(self, dName): #Метод для видалення запису з словника 
        return f"Delet - {dName} {self.data.pop(dName)}" #Повертаю результат і видаляю користувача



class Field(): #Базовий клас
    def __init__(self, fd_Name, fd_Phone=None) -> None:
        self.fd_Name = fd_Name
        self.fd_Phone = fd_Phone

class Name(Field): #Клас для імені 
    def __init__(self, valName) -> None:
        self.valName = valName        
    
    def __str__(self) -> str:
        return self.valName

class Phone(Field): #Клас для телефону
    def __init__(self, valPhone) -> None:
        self.valPhone = valPhone
    
    def phone_validation(self): #Валідація номеру телефону
        if isinstance(self.valPhone, str) and len(self.valPhone) == 13 and self.valPhone.startswith("+380"): #Перевірка номера телефону
            return self.valPhone
        else: return print("Wrong phone format")

class Birthday(Field): #Клас для дати народження ###########################
    def __init__(self, valBirt):
        try:
            pass
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")




class Record: #Клас для зберігання інформації про контакт
    def __init__(self, name):
        self.name = Name(name) #Зберігаю обєкт імені
        self.phones = None #Список для телефонів
        self.birthday = None #День народження
        self.dictREC = {} #Вихідний словник
    
    def dict_record(self): #Метод для створення словника
        self.dictREC = {self.name.valName: {
            "phone": self.phones,
            "birthday": self.birthday
            }}
        return self.dictREC #Вертаю словник




def add_user_book(addUser, User_book): #Функція додавання користувача до UserDict
    u = "".join(addUser) #Додаю ім'я зі списку до рядка
    if u: #Роблю перевірку на пусте значення
        rec = Record(u) #Створюю об'єкт класу Record
        User_book.add_record(rec.dict_record()) # І записую в UserDict
    else: print("!Add a username!") #Виводжу попередження що ім'я не введене


def add_phone_to_user(args, User_book): #Функція додавання до користувача телефону
    n, p = args #Розбиваю список
    p = Phone(p).phone_validation()
    if p != None:
        User_book.update_user(n, {"phone": p}) #Оновлюю телефон користувача


def add_birthday_to_user(args, User_book): #Функція додавання до користувача дня народження
    n, b = args #Розбиваю список
    User_book.update_user(n, {"birthday": b}) #Оновлюю ДН користувача


# #####################################################################################################################################
def parse_input(user_input): #Функція для парсингу команд
    cmd, *args = user_input.split() #Розбиваю команду
    cmd = cmd.strip().lower() #Записую команду в окрему змінну
    return cmd, *args #Повертаю команду і аргументи


def main(): #Основна функція з циклом 
    book = AddressBook() #Екземпляр класу AddressBook
    print("Welcome to the assistant bot!")
    while True: #Основний цикл для постійного запиту команд
        user_input = input("Enter a command: ") #Запитую команду
        command, *args = parse_input(user_input) #Зберігаю результат парсингу в змінні 

        if command in ["exit", "close"]: #Команди виходу з програми
            print("Good bye!")
            break
        
        elif command == "hello":
            print("Hello! \nHow can I help you?")
        
        elif command == "all": #Виводжу всі контакти з AddressBook
            print(book.data)
        
        elif command == "add": #Додаю користувача до AddressBook
           add_user_book(args, book)

        elif command == "add-phone": #Додаю телефон до користувача
            add_phone_to_user(args, book)
        
        elif command == "phone": #Виводжу телефон користувача
            up = "".join(args) #Додаю ім'я зі списку до рядка
            print(book.find_data_user(up, "phone")) #Шукаю телефон користувача в книзі
        
        elif command == "add-birthday": #Додаю день народження
            add_birthday_to_user(args, book)

        elif command == "show-birthday": #Виводжу день народження користувача
            ub = "".join(args) #Додаю ім'я зі списку до рядка
            print(book.find_data_user(ub, "birthday")) #Шукаю день народження користувача в книзі

        elif command == "birthdays":
            print(book.find_birthday_users_for_week())
        
        elif command == "q": print("break"); break
        else: #Помилкова команда
            print("Invalid command!!!")
        



if __name__ == "__main__": #
    main()
