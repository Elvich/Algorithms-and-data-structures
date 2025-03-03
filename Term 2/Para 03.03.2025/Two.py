import  abc

class Student(abc.ABC):
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @abc.abstractmethod
    def get_info(self): pass

    def matches_conditions(self, **conditions):
        return all(getattr(self, attribute, None) == value for attribute, value in conditions.items())


class Bachelor(Student):
    def __init__(self, first_name, last_name, age, course):
        super().__init__(first_name, last_name, age)
        self.course = course

    def get_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, Лет: {self.age}, Курс: : {self.course}")



class Master(Student):
    def __init__(self, first_name, last_name, age, specialization):
        super().__init__(first_name, last_name, age)
        self.specialization = specialization

    def get_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, Лет: {self.age}, Специальность: {self.specialization}")



class PhD(Student):
    def __init__(self, first_name, last_name, age, thesis_topic):
        super().__init__(first_name, last_name, age)
        self.thesis_topic = thesis_topic

    def get_info(self):
        print(f"Студент: {self.first_name} {self.last_name}, Лет: {self.age}, Тема дисертации: {self.thesis_topic}")





students = [
    Bachelor("Алексей", "Иванов", 20, 2),
    Bachelor("Мария", "Смирнова", 21, 3),
    Master("Дмитрий", "Козлов", 24, "Математика"),
    Master("Екатерина", "Васильева", 25, "Физика"),
    PhD("Иван", "Петров", 28, "Квантовые вычисления"),
    PhD("Ольга", "Сидорова", 30, "Искусственный интеллект"),
]

print("Вся информация о студентах:\n")
for student in students:
    student.get_info()

print("-" * 40)




search_name = "Екатерина"
search_course = 2

print(f"Поиск по имени '{search_name}' и курсу '{search_course}':\n")
found_students = [student for student in students if student.matches_conditions(first_name=search_name, course=search_course)]
if found_students:
    for student in found_students:
        student.get_info()
else:
    print("Такой студент не найден")