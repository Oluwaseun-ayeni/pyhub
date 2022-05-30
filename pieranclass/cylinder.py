class Cylinder(object):
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume(self):
        h = self.height
        r = self.radius

        return 3.142 * r ** 2 * h

    def surface_area(self):
        h = self.height
        r = self.radius

        return 2 * 3.142 * r ** 2 + 2 * 3.142 * r * h


c = Cylinder(2, 3)

print(c.volume())
print(c.surface_area())
