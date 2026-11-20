#!/usr/bin/env python3

import timeit as t
import sys


def long_list():
    emails = ['john@gmail.com', 'james@gmail.com',
              'alice@yahoo.com', 'anna@live.com',
              'philipp@gmail.com']
    required_list = emails * 5
    return required_list


def gmail_with_loop():
    data_list = long_list()
    final_list = []
    for email in data_list:
        if '@gmail.com' in email:
            final_list.append(email)
    return final_list



def gmail_with_comprehension():
    data_list = long_list()
    # Используем списковое включение для фильтрации адресов Gmail
    final_list = [email for email in data_list if '@gmail.com' in email]
    return final_list


def in_gmail(email):
    if '@gmail.com' in email:
        return email


def gmail_with_map():
    data_list = long_list()
    final_list = map(in_gmail, data_list)
    return final_list


def gmail_with_filter():
    data_list = long_list()
    final_list = filter(in_gmail, data_list)
    return final_list


def benchmark(function_name, number_of_calls):
    number_of_calls = int(number_of_calls)
    func_map = {
        'loop': gmail_with_loop,
        'list_comprehension': gmail_with_comprehension,
        'map': gmail_with_map,
        'filter': gmail_with_filter
    }

    if function_name in func_map:
        timer = t.timeit(func_map[function_name], number=number_of_calls)
        return timer
    else:
        raise ValueError("Invalid function name. Choose from: loop, list_comprehension, map, filter.")


def main():
    if len(sys.argv) != 3:
        print("Использование: ./benchmark.py <имя_функции> <количество_вызовов> ")
        print("Функции:", "loop", "list_comprehension", "map", "filter", sep='\n')
        sys.exit(1)

    func_name = sys.argv[1]
    calls = sys.argv[2]

    try:
        timer = benchmark(func_name, calls)
        print(timer)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
