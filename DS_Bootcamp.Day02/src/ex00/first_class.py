class must_read:

    filename = 'data.csv'

    with open(filename, 'r') as file:
        for line in file:
            for char in line:
                print(char, end= '')
        print()

# Создаем экземпляр класса Must_read для выполнения чтения файла
if __name__ == "__main__":
    example = must_read()
