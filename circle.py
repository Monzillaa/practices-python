from math import pi
class Circle:
    def __init__(self, radio):
        self.radio = radio
    @property
    def area(self):
            return pi * (self.radio ** 2)
c = Circle(25)
print(c.area)