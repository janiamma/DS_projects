#!/usr/bin/env python3

import timeit as t


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


def benchmark(func_name, calls):
    calls = int(calls)
    func_dict = {
        'loop': gmail_with_loop,
        'list_comprehension': gmail_with_comprehension,
        'map': gmail_with_map
    }

    if func_name in func_dict:
        timer = t.timeit(func_dict[func_name], number=calls)
        return timer
    else:
        raise ValueError("Invalid function name. Choose from: loop, list_comprehension, map.")


def calculations():
    # Измеряем время выполнения функции
    number_of_calls = 9000000
    times_dict = {}

    for method in ['loop', 'list_comprehension', 'map']:
        times_dict[method] = benchmark(method, number_of_calls)

    min_time = min(times_dict, key=times_dict.get)
    result = f'it is better to use a {min_time}'
    print(result)

    sorted_values = sorted(times_dict.values())
    ascend_times = ' vs '.join([str(value) for value in sorted_values])
    print(ascend_times)


if __name__ == "__main__":
    calculations()
