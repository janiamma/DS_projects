import sys
import os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self, has_header=True):
        data = []
        if not os.path.exists(self.file_path):
            return f"The file {self.file_path} does not exist."

        try:
            with open(self.file_path, 'r') as file:
                first_line = file.readline().strip()  # Читаем первую строчку
                if first_line:
                    if not self.validate_header(first_line): # Проверяем, заголовок ли это
                        has_header=False
                        if self.validate_line(first_line):
                            data.append(self.to_integer(first_line))  # Добавляем первую строку в данные, если это не заголовок
                        else:
                            raise ValueError("File structure: header is not valid")
                else:
                    raise ValueError("The file is empty.")
                # Читаем остальные строки
                for line in file:
                    line = line.strip()
                    if not self.validate_line(line):
                        raise ValueError("Invalid file structure: line does not match expected values.")
                    data.append(self.to_integer(line))  # Добавляем список целых чисел в data
            return data
        except ValueError as e:
            return str(e)

    def validate_header(self, header):
        # Проверяем, что заголовок содержит две строки, разделенные запятой
        return len(header.split(',')) == 2 and header not in ["0,1", "1,0"]
    def validate_line(self, line):
        # Проверяем, что строка содержит либо 0, либо 1, разделенные запятой
        return line in ["0,1", "1,0"]
    def to_integer(self, line):
        string_values = line.split(',')
        # Преобразуем каждую строку в целое число и добавляем в список
        int_values = []
        for value in string_values:
            int_values.append(int(value))  # Преобразуем строку в int и добавляем в список
        return int_values

    class Calculations:
        def counts(data):
            heads = sum(1 for row in data if row[0] == 1)
            tails = sum(1 for row in data if row[1] == 1)
            return heads, tails

        def fractions(heads, tails):
            total = heads + tails
            head_fraction = (heads / total) * 100
            tail_fraction = (tails / total) * 100
            return head_fraction, tail_fraction
def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 first_nest.py ../ex00/data.csv")
            sys.exit(1)

        file_path = sys.argv[1]
        research_object = Research(file_path)
        data = research_object.file_reader()  # Получаем данные из файла
        if isinstance(data, str):  # Проверяем, не является ли data сообщением об ошибке
            print(data)
            sys.exit(1)
        print(data)

        # Выполняем расчеты
        counts = Research.Calculations.counts(data)
        print(counts[0], counts[1])

        fractions = Research.Calculations.fractions(*counts)
        print(fractions[0], fractions[1])  # Выводим доли в процентах
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()