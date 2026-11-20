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
    # Используем списковое включение для фильтрации адресов gmail
    final_list = [email for email in data_list if '@gmail.com' in email]
    return final_list


def main():
    # Измеряем время выполнения функции
    number_of_calls = 9000000
    loop_timer = t.timeit(gmail_with_loop, number=number_of_calls)
    comprehension_timer = t.timeit(gmail_with_comprehension, number=number_of_calls)
    time_difference = comprehension_timer - loop_timer

    if time_difference <= 0:
        result = "it is better to use a list comprehension"
    else:
        result = "it is better to use a loop"

    print(result)
    print(f'{min(comprehension_timer, loop_timer)} vs {max(comprehension_timer, loop_timer)}')


if __name__ == "__main__":
    main()
