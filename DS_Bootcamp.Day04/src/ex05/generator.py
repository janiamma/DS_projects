#!/usr/bin/env python3

import sys
import os
import time


# Ссылка для скачивания большого датафайла:
# https://drive.google.com/file/d/1KZREmkar-jMte53y8CeIXrx6BY5Es7ji/view?usp=sharing

def read_file_generator(filename):
    # Генератор, который читает файл построчно
    with open(filename, 'r') as file:
        for line in file:
            yield line


def main():
    if len(sys.argv) != 2:
        print("Использование: ./generator.py <file_path>")
        print("Расположение файла: ratings.csv")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()
    # Создаем генератор
    file_ratings = read_file_generator(file_path)
    # Итерируем по генератору
    for _ in file_ratings:
        pass
    end_time = time.time()

    # Получаем использование памяти в GB
    mem_usage = 0
    try:
        if hasattr(sys, 'getwindowsversion'):
            import psutil
            process = psutil.Process(os.getpid())
            mem_usage = process.memory_info().rss / (1024 ** 3)
        else:
            # Для Windows
            import resource
            mem_usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 ** 3)
    except Exception as e:
        print(f"Memory measurement error: {e}")

    print(f"Peak Memory Usage: {mem_usage:.3f} GB")
    print(f"User Mode Time + System Mode Time: {end_time - start_time:.2f} seconds")


if __name__ == "__main__":
    main()
