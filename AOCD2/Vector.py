class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.aim = 0

    def add(self, other_vector):
        self.x = self.x + other_vector.x
        self.y = self.y + other_vector.y
        return self

    def addX(self, x):
        self.x = self.x + x
        self.y = self.y + (self.aim * x)
        return self

    def addY(self, y):
        self.aim = self.aim + y
        return self

    def __str__(self):
        return str([self.x, self.y, self.aim])