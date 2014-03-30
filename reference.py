'''
pass by reference test
'''


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = [self.x, self.y]  # this will not change

    def __str__(self):
        x, y = self.point
        return '(%s, %s)' % (x, y)

    @property
    def point_property(self):
        return (self.x, self.y)


class Line(object):
    def __init__(self, points):
        self.points = points

    def change(self):
        for p in self.points:
            t = p
            t.x = 0

    def print_points(self):
        print [str(p) for p in self.points]


points = [(1, 2), (3, 4)]

temp = []
for p in points:
    temp.append(Point(*p))

line = Line(temp)
line.print_points()
line.change()
line.print_points()  # not changed?

print [p.point_property for p in temp]  # do changed
