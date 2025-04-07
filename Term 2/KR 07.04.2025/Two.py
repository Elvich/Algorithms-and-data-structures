class Phonebook:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    def display_info(self):
        raise NotImplementedError("Этот метод должен быть переопределен в дочерних классах")

    def matches_name(self, search_name):
        return self.name.lower() == search_name.lower()


class Person(Phonebook):
    def __init__(self, name, address, phone):
        super().__init__(name, address, phone)

    def display_info(self):
        print(f"Фамилия: {self.name}")
        print(f"Адрес: {self.address}")
        print(f"Номер телефона: {self.phone}")
        


class Organization(Phonebook):
    def __init__(self, name, address, phone, fax, contact_person):
        super().__init__(name, address, phone)
        self.fax = fax
        self.contact_person = contact_person

    def display_info(self):
        print(f"Название организации: {self.name}")
        print(f"Адрес: {self.address}")
        print(f"Телефон: {self.phone}")
        print(f"Факс: {self.fax}")
        print(f"Контактное лицо: {self.contact_person}")



class Friend(Phonebook):
    def __init__(self, name, address, phone, birth_date):
        super().__init__(name, address, phone)
        self.birth_date = birth_date

    def display_info(self):
        print(f"Фамилия: {self.name}")
        print(f"Адрес: {self.address}")
        print(f"Номер телефона: {self.phone}")
        print(f"Дата рождения: {self.birth_date}")

def display_all_entries(entries):
    for entry in entries:
        entry.display_info()
        print("-" * 30)


def search_by_name(entries, search_name):
    matching_entries = [entry for entry in entries if entry.matches_name(search_name)]
    if not matching_entries:
        print(f"Записи с фамилией '{search_name}' не найдены.")
    else:
        print(f"Найденные записи для фамилии '{search_name}':")
        display_all_entries(matching_entries)


# Создание списка записей
entries = [
    Person("Иванов", "Москва, ул. Пушкина, д. 10", "+7 (999) 123-45-67"),
    Organization("ООО 'Рога и Копыта'", "Санкт-Петербург, Невский пр., д. 25", "+7 (812) 111-11-11", "+7 (812) 222-22-22", "Петров А.Б."),
    Friend("Сидоров", "Екатеринбург, ул. Ленина, д. 5", "+7 (999) 987-65-43", "15.06.1990"),
    Person("Петров", "Казань, ул. Баумана, д. 15", "+7 (999) 444-44-44"),
    Friend("Кузнецов", "Новосибирск, ул. Советская, д. 8", "+7 (999) 555-55-55", "20.12.1985")
]

# Вывод полной информации о записях
print("Полная информация о записях в телефонном справочнике:")
display_all_entries(entries)

# Поиск записи по фамилии
search_name = input("Введите фамилию для поиска: ")
search_by_name(entries, search_name)