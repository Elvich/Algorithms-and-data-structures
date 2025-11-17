def main():
    filename = input("Введите имя файла: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Файл не найден.")
        return

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Количество строк: {line_count}")
    print(f"Количество слов: {word_count}")
    print(f"Количество символов: {char_count}")


if __name__ == "__main__":
    main()

