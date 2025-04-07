from functools import reduce

students = [
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Дмитрий", "age": 19, "grades": [3, 3, 2, 4]},
    {"name": "Евгения", "age": 21, "grades": [5, 5, 5, 5]},
    {"name": "Александр", "age": 22, "grades": [4, 5, 3, 4]},
    {"name": "Ольга", "age": 22, "grades": [5, 3, 5, 3]}
]

upper_case_names = list(map(lambda student: student["name"].upper(), students))
print("Список имён в верхнем регистре:", upper_case_names)
print()


filtered_students = list(filter(lambda student: student["age"] > 20, students))
print("Студенты старше 20 лет:")
for student in filtered_students:
    print(student)
print()


total_sum, total_count = reduce(
    lambda acc, student: (
        acc[0] + sum(student["grades"]),
        acc[1] + len(student["grades"])
    ),
    students,
    (0, 0)
)

average_grade = total_sum / total_count if total_count != 0 else 0
print(f"Общий средний балл всех студентов: {average_grade:.2f}")