# coding=utf-8
import matplotlib.pyplot as plt
from scipy import optimize
import numpy as np

a = 0.0
b = 0.0


def f(x):
    return ((x + a) ** 2) - b


def g(x):
    return abs(f(x))


def find_function_min(y):
    arg_min, val_min, iter_min = optimize.golden(y, full_output=True)
    return val_min


def print_graph():
    x = np.arange(0.0, 10.0, 0.01)
    f_x = f(x)
    g_x = g(x)
    fig = plt.figure()
    ax_f = fig.add_subplot(2, 1, 1)
    ax_f.plot(x, f_x, 'r', label="f(x)")
    ax_f.set_title('f(x)')
    ax_g = fig.add_subplot(2, 1, 2)
    ax_g.plot(x, g_x, 'g', label="g(x)")
    ax_g.set_title('g(x)')
    plt.show()


def minimums_of_functions(arg_a, arg_b):
    # --------------------
    # Реализовать программу, которая вычисляет минимальное значение функций f(x) и g(x) с использованием пакета
    # scipy.optimize.golden(). Постройте график функций в диапазоне [-10;10] с помощью пакета matplotlib.
    # --------------------
    global a
    a = arg_a
    global b
    b = arg_b
    val_min_f = find_function_min(f)
    val_min_g = find_function_min(g)
    print "Минимальное значение функции f(x) = ", val_min_f
    print "Минимальное значение функции g(x) = ", val_min_g
    print_graph()
    return val_min_f, val_min_g


minimums_of_functions(1, 50)
