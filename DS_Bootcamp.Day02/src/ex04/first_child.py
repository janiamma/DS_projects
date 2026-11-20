import sys
import os
from random import randint

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
                if first_line:  # Проверяем, что первая строка не пустая
                    if not self.validate_header(first_line):  # Проверяем, заголовок ли это
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
                    if not line:
                        continue
                    if not self.validate_line(line):
                        raise ValueError("Invalid file structure: line does not match expected values.")
                    data.append(self.to_integer(line))  # Добавляем список целых чисел в data
            return data
        except ValueError as e:
            return str(e)

    def validate_header(self, header):
        return len(header.split(',')) == 2 and header not in ["0,1", "1,0"]

    def validate_line(self, line):
        return line in ["0,1", "1,0"]

    def to_integer(self, line):
        string_values = line.split(',')
        int_values = []
        for value in string_values:
            int_values.append(int(value))
        return int_values

class Calculations:
    def __init__(self, data):
        self.data = data

    def counts(self):
        heads = sum(1 for row in self.data if row[0] == 1)
        tails = sum(1 for row in self.data if row[1] == 1)
        return heads, tails

    def fractions(self):
        heads, tails = self.counts()
        total = heads + tails
        if total == 0:
            return 0, 0
        head_fraction = (heads / total) * 100
        tail_fraction = (tails / total) * 100
        return head_fraction, tail_fraction

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)

    def predict_random(self, n):
        predictions = []
        for _ in range(n):
            first_element = randint(0, 1)  # Генерируем первый элемент
            second_element = 1 - first_element  # Второй элемент зависит от первого
            prediction = [first_element, second_element]
            predictions.append(prediction)
        return predictions

    def predict_last(self):
        return self.data[-1] if self.data else None

def main():
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 first_child.py ../ex00/data.csv")
            sys.exit(1)

        file_path = sys.argv[1]
        research_object = Research(file_path)
        data = research_object.file_reader()  # Получаем данные
        if isinstance(data, str):  # Проверяем сообщение об ошибке
            print(data)
            sys.exit(1)
        print(data)

        # Создаем объект Analytics
        calculations = Analytics(data)
        counts = calculations.counts()
        print(counts)

        fractions = calculations.fractions()
        print(fractions)

        # Получаем предсказания
        random_predictions = calculations.predict_random(3)
        print(random_predictions)

        # Получаем последнее предсказание
        last_prediction = calculations.predict_last()
        print(last_prediction)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
