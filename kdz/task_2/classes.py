class Efficiency:
    def __init__(self, x, p):
        self.x = x
        self.p = p


class Project:
    b = None
    F = None

    def __init__(self, efficiency, name, M, sigma):
        self.efficiency = efficiency
        self.name = name
        self.M = M
        self.sigma = sigma

    def set_b(self, b):
        self.b = b

    def set_f(self, F):
        self.F = F
