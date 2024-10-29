
from collections import UserDict

class AddressBook(UserDict): #Клас для словника
    
    def add_record(self, data): #Метод для додавання словника до self.data
        super().update(data) #Додаю словник через super
    
    def find(self, fName): #Шукаю в словнику по імені
        return f"Find: {fName} {self.data.get(fName)}" #Повертаю результат
    
    def delete(self, dName): #Метод для видалення запису з словника 
        return f"Delet - {dName} {self.data.pop(dName)}" #Повертаю результат і видаляю контакт
    
    def update_user(self, uUser): #Метод для оновлення запису в словнику
        for d in self.data:
            if uUser == d:
                pass
         
        

book = AddressBook() #Екземпляр класу AddressBook



class Field(): #Базовий клас
    def __init__(self, fd_Name, fd_Phone=None) -> None:
        self.fd_Name = fd_Name
        self.fd_Phone = fd_Phone


class Name(Field): #Клас для імені 
    def __init__(self, valName) -> None:
        self.valName = valName        


class Phone(Field): #Клас для телефону
    def __init__(self, valPhone) -> None:
        self.valPhone = valPhone
    
    def phone_validation(self): #Валідація номеру телефону
        if isinstance(self.valPhone, str) and len(self.valPhone) == 13 and self.valPhone.startswith("+380"): #Перевірка номера телефону
            return self.valPhone



class Record: #Клас для зберігання інформації про контакт
    def __init__(self, name):
        self.name = Name(name) #Зберігаю обєкт імені
        self.phones = [] #Список для телефонів
        self.birthday = None
        
    def add_phone(self, num_phone): #Метод для додавання телефону
        self.num_phone = Phone(num_phone).phone_validation() #Зберігаю обєкт телефону
        self.phones.append(self.num_phone) #Додаю до списку номер
        
    def edit_phone(self, sPhone, newPhone): #Метод для заміни номера телефону
        for ph in self.phones: # Пробігаюсь по циклу
            if ph == sPhone: #Шукаю співпадіння
                self.phones.pop() #Видаляю номер який знайшов
                self.phones.append(newPhone) #Добаляю новий номер        
        
    def dict_record(self): #Метод для створення словника
        self.dt_r = {self.name.valName: self.phones} #Додаю до словника
        return self.dt_r #Вертаю словник




dima_record = Record("Dima") #Екземпляр класу Record
dima_record.add_phone("+55555") #Додаю номер до контакту
dima_record.add_phone("+380333333333") #Додаю номер до контакту
# dima_record.add_birthday("25.04.1999") #Додаю дату народження


vika_record = Record("Vika") #Екземпляр класу Record
vika_record.add_phone("+380555596438") #Додаю номер до контакту
vika_record.add_phone("+380123456789") #Додаю номер до контакту
vika_record.edit_phone("+380123456789", "+380222333344") #Замінюю номер телефону


book.add_record(dima_record.dict_record()) #Додаю контакт до словника
book.add_record(vika_record.dict_record()) #Додаю контакт до словника
print(book, "\n") #Виводжу весь словник


for name, record in book.data.items(): #Виведення всіх записів з основної книги
        print(name, record)
        
book.update_user("Dima")
    

