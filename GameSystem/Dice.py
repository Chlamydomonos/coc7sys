import numpy as np


class Dice:
    def __init__(self, d3s, d4s, d6s, d8s, d10s, d12s, d20s, d100s, const):
        self.d3s = d3s
        self.d4s = d4s
        self.d6s = d6s
        self.d8s = d8s
        self.d10s = d10s
        self.d12s = d12s
        self.d20s = d20s
        self.d100s = d100s
        self.const = const

    def throw(self):
        d3r = np.sum(np.random.randint(1, 3, size=self.d3s))
        d4r = np.sum(np.random.randint(1, 4, size=self.d4s))
        d6r = np.sum(np.random.randint(1, 6, size=self.d6s))
        d8r = np.sum(np.random.randint(1, 8, size=self.d8s))
        d10r = np.sum(np.random.randint(1, 10, size=self.d10s))
        d12r = np.sum(np.random.randint(1, 12, size=self.d12s))
        d20r = np.sum(np.random.randint(1, 20, size=self.d20s))
        d100r = np.sum(np.random.randint(1, 100, size=self.d100s))
        return d3r + d4r + d6r + d8r + d10r + d12r + d20r +d100r + self.const

    def __add__(self, other):
        if isinstance(other, Dice):
            return Dice(self.d3s + other.d3s, self.d4s + other.d4s, self.d6s + other.d6s, self.d8s + other.d8s,
                        self.d10s + other.d10s, self.d12s + other.d12s, self.d20s + other.d20s, self.d100s + other.d100s,
                        self.const + other.const)
        else:
            return Dice(self.d3s, self.d4s, self.d6s, self.d8s, self.d10s, self.d12s, self.d20s, self.d100s,
                        self.const + other)

    def __radd__(self, other):
        if isinstance(other, Dice):
            return Dice(self.d3s + other.d3s, self.d4s + other.d4s, self.d6s + other.d6s, self.d8s + other.d8s,
                        self.d10s + other.d10s, self.d12s + other.d12s, self.d20s + other.d20s,
                        self.d100s + other.d100s,
                        self.const + other.const)
        else:
            return Dice(self.d3s, self.d4s, self.d6s, self.d8s, self.d10s, self.d12s, self.d20s, self.d100s,
                        self.const + other)

    def __mul__(self, other):
        return Dice(self.d3s * other, self.d4s * other, self.d6s * other, self.d8s * other, self.d10s * other,
                    self.d12s * other, self.d20s * other, self.d100s * other, self.const * other)

    def __rmul__(self, other):
        return Dice(self.d3s * other, self.d4s * other, self.d6s * other, self.d8s * other, self.d10s * other,
                    self.d12s * other, self.d20s * other, self.d100s * other, self.const * other)


D3 = Dice(1, 0, 0, 0, 0, 0, 0, 0, 0)
D4 = Dice(0, 1, 0, 0, 0, 0, 0, 0, 0)
D6 = Dice(0, 0, 1, 0, 0, 0, 0, 0, 0)
D8 = Dice(0, 0, 0, 1, 0, 0, 0, 0, 0)
D10 = Dice(0, 0, 0, 0, 1, 0, 0, 0, 0)
D12 = Dice(0, 0, 0, 0, 0, 1, 0, 0, 0)
D20 = Dice(0, 0, 0, 0, 0, 0, 1, 0, 0)
D100 = Dice(0, 0, 0, 0, 0, 0, 0, 1, 0)
