class Book:
    def __init__(self, name, year, author = "Anonim", publishing = "none"):
        self.name = name
        self.author = author
        self.publishing = publishing
        self.year = year

    def get_info(self):
        text = f"Книга {self.name} была написана в {self.year} году, Автрор - {self.author}."
        return text if self.publishing == "none" else text + f" Издательство - {self.publishing}."


bk1 = Book("Ведьмак последнее желание", 1996, "Анджей Сапковский", "АСТ")
bk2 = Book("Белые ночи", 1848, "Фёдор Михайлович Достоевский")
bk3 = Book("Пикник на обочине", 1972, "братья Стругацкие", "Молодая гвардия")
bk4 = Book("Одиссея капитана Блада", 1922, "Рафаэль Сабатини", "Houghton Mifflin Harcourt")
bk5 = Book("Мастер и Маргарита", "1940", "Михаил Булгаков")

print(bk1.get_info())
print(bk2.get_info())
print(bk3.get_info())
print(bk4.get_info())
print(bk5.get_info())

