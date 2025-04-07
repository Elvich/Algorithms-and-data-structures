students = [
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Дмитрий", "age": 19, "grades": [3, 3, 2, 4]},
    {"name": "Евгения", "age": 21, "grades": [5, 5, 5, 5]},
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Ольга", "age": 22, "grades": [5, 3, 5, 3]}
]

upper_case_names = list(map(lambda student: student["name"].upper(), students))
print("Список имён в верхнем регистре:", upper_case_names)


filtered_students = list(filter(lambda student: student["age"] > 20, students))
print("Студенты старше 20 лет:")
for student in filtered_students:
    print(student)