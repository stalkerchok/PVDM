# coding=utf-8
import numpy as np

alpha = 0.6


def make_decision(A, alpha_value):
    # --------------------
    # Планируется строительство одного из 4х типов промышленного предприятия. Эффективность каждого типа предприятия
    # зависит от различных факторов. Предполагается, что выделено 4 различных состояния, каждое из которых означает
    # определенное сочетание внешних факторов, влияющих на эффективность строящегося объекта. Экономическая
    # эффективность отдельных типов предприятия задана матрицей А.
    # Принять решение о выборе типа предприятия на основе матрицы «голосования», используя критерии Вальда, Сэвиджа,
    # Гурвица ( ), Лапласа.
    # --------------------
    global alpha
    alpha = alpha_value
    print 'Матрица A:\n', A
    decision_matrix = [0]*len(A)
    wald_decisions = wald(A)
    savage_decisions = savage(A)
    hurwitz_decisions = hurwitz(A)
    laplace_decisions = laplace(A)
    decision_matrix = add_decisions(wald_decisions, decision_matrix)
    decision_matrix = add_decisions(savage_decisions, decision_matrix)
    decision_matrix = add_decisions(hurwitz_decisions, decision_matrix)
    decision_matrix = add_decisions(laplace_decisions, decision_matrix)
    print 'Матрица голосования:\n', decision_matrix
    # Из матрицы голосования выбираются все максимальные элементы
    maximums = [i for i in range(len(decision_matrix)) if decision_matrix[i] == max(decision_matrix)]
    print 'Выбрано преприятие: ', maximums
    if len(maximums) > 1:
        print 'По результатам вычислений выбрано несколько предприятий, требуется дополнительное исследование.'


def wald(A):
    print 'критерии Вальда'
    min_a = np.min(A, axis=1)
    print 'Минимальные значения для каждой строки:', min_a
    max_in_min_a = max(min_a)
    print 'Максимальное значение из минимальных значений для каждой строки:', max_in_min_a
    strategy = np.where(min_a == max_in_min_a)
    print 'Выбраны стратегии:', strategy[0]
    return strategy[0]


def savage(A):
    print 'Критерий Севиджа'
    max_a = np.max(A, axis=0)
    print 'Максимальные значения для каждого столбца:', max_a
    R = A.copy()
    for i in range(len(A)):
        for j in range(len(A[i])):
            R[i][j] = max_a[j] - R[i][j]
    print 'Матрица R:\n', R
    max_a = np.max(R, axis=1)
    print 'Максимальные значения для каждой строки:', max_a
    min_in_max_a = min(max_a)
    print 'Минимальное значение из максимальных значений для каждой строки:', min_in_max_a
    strategy = np.where(max_a == min_in_max_a)
    print 'Выбраны стратегии:', strategy[0]
    return strategy[0]


def hurwitz(A):
    print 'Критерий Гурвица'
    max_a = np.max(A, axis=1)
    print 'Максимальные значения для каждой строки:', max_a
    min_a = np.min(A, axis=1)
    print 'Минимальные значения для каждой строки:', min_a
    hurwitz_matrix = alpha*min_a + (1 - alpha)*max_a
    print 'Матрица Гурвица:\n', hurwitz_matrix
    max_a = max(hurwitz_matrix)
    print 'Максимальное значение в матрице Гурвица:', max_a
    strategy = np.where(hurwitz_matrix == max_a)
    print 'Выбраны стратегии:', strategy[0]
    return strategy[0]


def laplace(A):
    print 'Критерий Лапласа'
    n = len(A)
    D = A.copy().astype(float)
    D = D/n
    print 'Матрица D\n', D
    sum_d = np.sum(D, axis=1)
    print 'Суммы строк матрицы D:', sum_d
    max_d = max(sum_d)
    print 'Максимальная сумма строк:', max_d
    strategy = np.where(sum_d == max_d)
    print 'Выбраны стратегии:', strategy[0]
    return strategy[0]


def add_decisions(decisions, matrix):
    # --------------------
    # На основе чисел из массива decisions увеличивает на 1 элементы массива matrix
    # Пример.
    # На вход метода подаётся: decisions = [1, 2] matrix = [0, 0, 0, 0]
    # На выходе метода получаем: matrix = [0, 1, 1, 0]
    # --------------------
    for decision in decisions:
        matrix[decision] = matrix[decision] + 1
    return matrix


A_matrix = np.array([10, 6, 3, 2, 10, 5, 4, 8, 7, 7, 2, 3, 3, 8, 6, 5])
# A_matrix = np.array([10, 6, 3, 2, 10, 5, 4, 8, 7, 7, 2, 3])
A_matrix = A_matrix.reshape(4, 4)
make_decision(A_matrix, 0.6)
