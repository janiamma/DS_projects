#!/usr/bin/env python3

import timeit as t
import sys
from functools import reduce


def square_with_loop(number):
    summa_kwadratow = 0
    diapason = int(number) + 1
    for element in range(int(diapason)):
        summa_kwadratow += element ** 2
    return summa_kwadratow


def my_sum(a, b):
    return b * b + a


def square_with_reduce(number):
    return reduce(my_sum, range(1, int(number) + 1), 0)


def benchmark(func_name, calls, number):
    calls = int(calls)
    number = int(number)
    func_map = {
        'loop': square_with_loop,
        'reduce': square_with_reduce
    }

    if func_name in func_map:
        timer = t.timeit(lambda: func_map[func_name](number), number=calls)
        return timer
    else:
        raise ValueError("S21_Error: Invalid function name. Choose from: loop, reduce.")


def main():
    if len(sys.argv) != 4:
        print("Использование: ./benchmark.py <имя_функции> <количество_вызовов> <число>")
        print("Функции:", "loop", "reduce", sep='\n')
        sys.exit(1)

    func_name = sys.argv[1]
    calls = sys.argv[2]
    number = sys.argv[3]

    try:
        timer = benchmark(func_name, calls, number)
        print(timer)
    except Exception as e:
        print(e)
        sys.exit(1)


if __name__ == "__main__":
    main()
