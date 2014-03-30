from sys import argv
import ast


class Building(object):
    def __init__(self, l, h, r):
        self.left = l
        self.right = r
        self.height = h
        self.line = (l, h, r)

    def contain_left(self, another):
        return self.left <= another.left < self.right

    def contain_right(self, another):
        return self.left < another.right <= self.right

    def next_to(self, another):
        return self.right == another.left


class SkyLine(object):
    def __init__(self, building):
        self.buildings = [building]

    def find(self, new_building):
        begin_building = None
        end_building = None
        for building in self.buildings:
            if building.contain_left(new_building):
                begin_building = building
                break
        for building in self.buildings:
            if building.contain_right(new_building):
                end_building = building
                break
        return begin_building, end_building

    def add_building(self, new_building):
        begin_building, end_building = self.find(new_building)
        self.merge(begin_building, end_building, new_building)

    def merge(self, begin_building, end_building, new_building):
        if (begin_building or end_building) is None:
            self.insert(new_building)

    def get_sky_line(self):
        previous = self.buildings.pop(0)
        sky_line = [previous.left, previous.height]
        for building in self.buildings:
            if previous.next_to(building):
                sky_line += [building.left, building.height]
            else:
                sky_line += [previous.right, 0, building.left, building.height]
            previous = building
        sky_line += [building.right, 0]
        sky_line = map(str, sky_line)
        return ' '.join(sky_line)

    def insert(self, new_building):
        for i, building in enumerate(self.buildings):
            if new_building.right <= building.left:
                self.buildings.insert(i, new_building)
                break
        else:
            self.buildings.append(new_building)


def to_buildings(one):
    buildings = []
    for building in one:
        building = Building(*ast.literal_eval(building))
        buildings.append(building)
    return buildings


def to_sky_line(buildings):
    building = buildings.pop(0)
    sky_line = SkyLine(building)
    for building in buildings:
        sky_line.add_building(building)
    return sky_line.get_sky_line()


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        if one.startswith('#'):
            continue
        buildings = to_buildings(one.split(';'))
        print to_sky_line(buildings)
f.close()
