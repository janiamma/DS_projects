import sys
import os

class Research:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_reader(self):
        content = ""
        # Проверяем, существует ли файл
        if not os.path.exists(self.file_path):
            return f"The file {self.file_path} does not exist."

        try:
            with open(self.file_path, 'r') as file:
                # Читаем заголовок
                header = file.readline().strip()
                content += header + "\n"
                if not self.validate_header(header):
                    raise ValueError("Invalid file structure: header is not valid.")
                    sys.exit(1)

                # Читаем остальные строки
                for line in file:
                    line = line.strip()
                    if not self.validate_line(line):
                        raise ValueError("Invalid file structure: line does not match expected values.")
                        sys.exit(1)
                    content += line + "\n"  # Сохраняем содержимое в переменной
            return content.strip()
        except ValueError as e:
            return str(e)

    def validate_header(self, header):
        # Проверяем, что заголовок содержит две строки, разделенные запятой
        return len(header.split(',')) == 2
    def validate_line(self, line):
        # Проверяем, что строка содержит либо 0, либо 1, разделенные запятой
        return line in ["0,1", "1,0"]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 first_constructor.py ../ex00/data.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    my_object = Research(file_path)
    my_file = my_object.file_reader()
    if my_file:                         # Проверяем, что my_file не пустое
        print(my_file)