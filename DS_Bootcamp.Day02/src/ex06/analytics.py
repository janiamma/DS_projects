import sys
import os
from random import randint
import logging
import requests

logging.basicConfig(
    filename='analytics.log',
    level=logging.DEBUG,
    format='%(asctime)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

class Research:
    def __init__(self, file_path, url, chat_id):
        self.file_path = file_path
        self.url = url
        self.chat_id = chat_id
        logging.info(f"Запуск исследования файла {self.file_path}")

    def file_reader(self, has_header=True):
        logging.debug("Чтение файла")
        data = []
        if not os.path.exists(self.file_path):
            logging.error(f"Ошибка чтения файла: файл {self.file_path} не существует")
            return f"The file {self.file_path} does not exist."
        
        try:
            with open(self.file_path, 'r') as file:
                first_line = file.readline().strip()  # Читаем первую строчку
                if first_line:  # Проверяем, что первая строка не пустая
                    if not self.validate_header(first_line):  # Проверяем, заголовок ли это
                        has_header=False
                        logging.info("Заголовок отсутствует")
                        if self.validate_line(first_line):
                            data.append(self.to_integer(first_line))  # Добавляем первую строку в данные, если это не заголовок
                        else:
                            raise ValueError("File structure: header is not valid")
                else:
                    raise ValueError("The file is empty.")

                # Читаем остальные строки
                for line in file:
                    line = line.strip()
                    if not line:  # Проверяем, что строка не пустая
                        continue
                    if not self.validate_line(line):
                        raise ValueError("Invalid file structure: line does not match expected values.")
                    data.append(self.to_integer(line))  # Добавляем список целых чисел в data
            logging.info("Файл успешно прочитан")
            return data
        except ValueError as e:
            logging.error(f"Ошибка файла - {e}")
            return str(e)

    def validate_header(self, header):
        logging.debug("Проверка заголовка")
        return len(header.split(',')) == 2 and header not in ["0,1", "1,0"]

    def validate_line(self, line):
        logging.debug("Проверка структуры строки")
        return line in ["0,1", "1,0"]

    def to_integer(self, line):
        logging.debug("Перевод строковых в числовой тип для последующих расчётов")
        string_values = line.split(',')
        int_values = []
        for value in string_values:
            int_values.append(int(value))
        return int_values

    def send_telegram_message(self, success):
        if success:
            message = "The report has been successfully created."
        else:
            message = "The report hasn’t been created due to an error."

        payload = {
            'chat_id': self.chat_id,
            'text': message
        }

        try:
            response = requests.post(self.url, json=payload)
            response.raise_for_status()  # Проверка на ошибки HTTP
            logging.info("Сообщение успешно отправлено в Telegram")
        except requests.exceptions.RequestException as e:
            logging.error(f"Ошибка при отправке сообщения в Telegram: {e}")

class Calculations:
    def __init__(self, data):
        self.data = data
        logging.debug("Запуск расчётов")

    def counts(self):
        logging.debug("Подсчёт голов и хвостов")
        heads = sum(1 for row in self.data if row[0] == 1)
        tails = sum(1 for row in self.data if row[1] == 1)
        logging.info(f"Подведены расчёты: голов={heads}, хвостов={tails}")
        return heads, tails

    def fractions(self):
        logging.debug("Подсчёт процентного распределения голов и хвостов")
        heads, tails = self.counts()
        total = heads + tails
        if total == 0:
            return 0, 0
        head_fraction = (heads / total) * 100
        tail_fraction = (tails / total) * 100
        logging.info(f"Подведены расчёты распредения: голов={head_fraction}%, хвостов={tail_fraction}%")
        return head_fraction, tail_fraction

class Analytics(Calculations):
    def __init__(self, data):
        super().__init__(data)
        logging.debug("Запуск аналитики")

    def predict_random(self, n):
        logging.debug(f"Предсказание следующих {n} элементов")
        predictions = []
        for _ in range(n):
            first_element = randint(0, 1)  # Генерируем первый элемент
            second_element = 1 - first_element  # Второй элемент зависит от первого
            prediction = [first_element, second_element]
            predictions.append(prediction)
        logging.info(f"Случайные предсказания сгенерированы: {predictions}")
        return predictions

    def predict_last(self):
        return self.data[-1] if self.data else None

    def save_file(self, data, file_name, extension):
        logging.debug(f"Сохранение отчёта в файл: {file_name}.{extension}")
        with open(f"{file_name}.{extension}", 'w') as file:
            file.write(data)
        logging.info(f"Отчёт сохранён в файл: {file_name}.{extension}")
