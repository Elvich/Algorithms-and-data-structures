class Employee:
    def __init__(self, first_name, second_name, post, salary):
        self.first_name = first_name
        self.second_name = second_name
        self.post = post
        self.salary = salary
        self.experience = 0

    def get_info(self):
        text = f"{self.first_name} {self.second_name} работает на должности {self.post}, за зарплату в {self.salary} рублей"
        text = text if self.experience == 0 else text + f". Его стаж - {self.experience} лет"
        return text

    def chek_salary(self):
        return "Выше базовой величины" if self.salary > 100000 else "Ниже базовой величины"

    def set_experience(self, experience):
        self.experience = experience

    def add_experience(self, experience):
        self.experience += experience


emp1 = Employee("Недима", "Необлочков", "Генеральный деректор", 60000)

print(emp1.get_info())
print(emp1.chek_salary())
print()

emp1.set_experience(10)
print(emp1.get_info())
print()

emp1.add_experience(1)
print(emp1.get_info())
print()

