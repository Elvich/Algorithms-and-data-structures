import os

isOpen = True

while isOpen:
    print("Выберете номер нужного задания \n")

    print("1. Проверка возможности составить треугольник")
    print("2. Проверка на остроугольный треугольник")
    print("3. Сложение действительных и разность мнимых частей комплексных чисел")
    print("4. Проверка анаграмм")
    print("5. Арифметическая прогрессия")
    print("6. Проверка наличия всех букв алфавита")
    print("7. Проверка вхождения одной строки в другую")
    print("8. Нахождение максимальной разницы")
    print("9. Следующий символ по алфавиту")
    print("10. Площадь треугольника по трём сторонам (формула Герона)")
    print("11. Разделение строки на две равные части")
    print("12. Проверка возможности получения палиндрома")
    print("13. Проверка чисел на корни уравнения")
    print("14. Сумма квадратов чисел")
    print("15. Геометрическая прогрессия")
    print("16. Закрыть \n")

    Choice = int(input("Введите ночер задачи: "))
    print("\n")

    if Choice == 16:
        isOpen = False
        break

    if Choice == 1:
        os.system('python3 One.py')
    elif Choice == 2:
        os.system('python3 Two.py')
    elif Choice == 3:
        os.system('python3 Three.py')
    elif Choice == 4:
        os.system('python3 Four.py')
    elif Choice == 5:
        os.system('python3 Five.py')
    elif Choice == 6:
        os.system('python3 Six.py')
    elif Choice == 7:
        os.system('python3 Seven.py')
    elif Choice == 8:
        os.system('python3 Eight.py')
    elif Choice == 9:
        os.system('python3 Nine.py')
    elif Choice == 10:
        os.system('python3 Ten.py')
    elif Choice == 11:
        os.system('python3 Eleven.py')
    elif Choice == 12:
        os.system('python3 Twelve.py')
    elif Choice == 13:
        os.system('python3 Thirteen.py')
    elif Choice == 14:
        os.system('python3 Fourteen.py')
    elif Choice == 15:
        os.system('python3 Fifteen.py')
    else:
        print("Такого задания нет. Повторите попытку")

    input("Нажмите Enter, чтобы продолжить")

    print("\n")