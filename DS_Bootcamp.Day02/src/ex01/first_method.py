class Research:
    def file_reader(self):
        filename = '../ex00/data.csv'
        content = ""

        with open(filename, 'r') as file:
            for line in file:
                for char in line:
                    content += char
        return content

if __name__ == "__main__":
    my_research = Research()
    my_file = my_research.file_reader()
    print(my_file)