#!/usr/bin/env python3

import timeit as t
from collections import Counter
import random


def random_values():
    return [random.randint(0, 100) for _ in range(1_000_000)]


def create_count_dict(values):
    count_dict = {i: 0 for i in range(101)}  # Инициализация словаря с ключами от 0 до 100
    for value in values:
        if value in count_dict:
            count_dict[value] += 1
    return count_dict


def my_top_10_common(values):
    dict_to_sort = create_count_dict(values)
    sorted_items = sorted(dict_to_sort.items(), key=lambda item: item[1], reverse=True)

    # Извлекаем только первые 10 элементов
    top_10 = sorted_items[:10]

    return top_10


# Создание словаря с подсчетом с использованием Counter
def create_count_dict_with_counter(values):
    return Counter(values)


# Получение 10 самых распространенных чисел
def get_top_10_common_with_counter(count_dict):
    return count_dict.most_common(10)


def benchmark():
    values = random_values() # генерируем случайные значения здесь
    count_dict = create_count_dict_with_counter(values)
    func_map = {
        'my function': create_count_dict,
        'Counter': create_count_dict_with_counter,
        'my top': my_top_10_common,
        'Counter\'s top': lambda: get_top_10_common_with_counter(count_dict)
    }

    for key, func in func_map.items():
        if key != "Counter's top":
            # Обычные функции: передаём values
            timer = t.timeit(lambda: func(values), number=1)
        else:
            # Для 'Counter's top' не передаём values
            timer = t.timeit(lambda: func(), number=1)
        print(f"{key}: {timer}")


if __name__ == "__main__":
    try:
        benchmark()
    except Exception as e:
        print(e)
