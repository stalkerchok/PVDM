# coding=utf-8
import math
import matplotlib.pyplot as plt
from classes import Efficiency, Project

E1 = Efficiency([2, 5, 8, 4], [0.1, 0.4, 0.1, 0.4])
E2 = Efficiency([2, 3, 4, 12], [0.5, 0.3, 0.1, 0.1])
E3 = Efficiency([3, 5, 8, 10], [0.3, 0.3, 0.2, 0.2])
E4 = Efficiency([1, 2, 4, 8], [0.1, 0.3, 0.1, 0.5])
E5 = Efficiency([8, 10, 1, 2], [0.1, 0.4, 0.4, 0.1])
E6 = Efficiency([4, 15, 20, 10], [0.4, 0.2, 0.1, 0.3])
E7 = Efficiency([5, 7, 10, 12], [0.2, 0.3, 0.3, 0.2])
E8 = Efficiency([1, 8, 2, 12], [0.5, 0.2, 0.2, 0.1])
E9 = Efficiency([7, 4, 10, 15], [0.2, 0.4, 0.2, 0.2])
E10 = Efficiency([20, 1, 2, 8], [0.2, 0.4, 0.2, 0.2])
E11 = Efficiency([14, 8, 3, 1], [0.1, 0.2, 0.3, 0.4])
E12 = Efficiency([18, 5, 1, 10], [0.1, 0.2, 0.5, 0.2])
E13 = Efficiency([17, 4, 8, 12], [0.1, 0.3, 0.4, 0.2])
E14 = Efficiency([19, 1, 5, 10], [0.1, 0.4, 0.2, 0.3])
E15 = Efficiency([13, 10, 4, 2], [0.3, 0.1, 0.1, 0.5])
E16 = Efficiency([12, 10, 9, 4], [0.1, 0.5, 0.2, 0.2])


def choose_project(efficiency_array):
    projects = create_projects(efficiency_array)
    print_projects(projects)
    print_graph(projects)


def create_projects(efficiency_array):
    projects = []
    count = 1
    for efficiency in efficiency_array:
        name = 'F' + str(count)
        M = calculate_m(efficiency.x, efficiency.p)
        sigma = calculate_sigma(efficiency.x, efficiency.p)
        projects.append(Project(efficiency, name, M, sigma))
        count = count + 1
    return projects


def calculate_m(x, p):
    M = 0
    for i in range(len(x)):
        M = M + x[i] * p[i]
    return M


def calculate_sigma(x, p):
    x_square = [i*i for i in x]
    D = calculate_m(x_square, p) - calculate_m(x, p) ** 2
    sigma = math.sqrt(D)
    return sigma


def print_graph(projects):
    M = []
    sigma = []
    for project in projects:
        M.append(project.M)
        sigma.append(project.sigma)
    plt.scatter(M, sigma)
    plt.show()


def print_projects(projects):
    print '=================================================================================='
    for project in projects:
        print 'name', project.name
        print 'efficiency', project.efficiency.__dict__
        print 'M', project.M
        print 'sigma', project.sigma
        print '=================================================================================='


choose_project([E2, E3, E8, E9, E10, E11, E12, E15, E10, E11, E1, E2, E4, E9, E12, E13])
