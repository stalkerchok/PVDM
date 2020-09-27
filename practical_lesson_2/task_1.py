# coding=utf-8
from generator.fibonacci import generate_sequence


def get_fibonacci_sequence(n):
    # --------------------
    # Реализовать программу для получения N чисел Фибоначчи.
    # Метод вычисления чисел должен располагаться в отдельном пакете.
    # Метод должен использовать генератор для вычисления N чисел.
    # --------------------
    fibonacci_sequence = list(generate_sequence(n))
    print(fibonacci_sequence)
    return fibonacci_sequence


get_fibonacci_sequence(10)
