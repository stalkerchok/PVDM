class Efficiency:
    def __init__(self, x, p):
        self.x = x
        self.p = p


class Project:
    def __init__(self, efficiency, name, M, sigma):
        self.efficiency = efficiency
        self.name = name
        self.M = M
        self.sigma = sigma
