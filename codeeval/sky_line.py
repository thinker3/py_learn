from sys import argv
import re


class Building(object):
    def __init__(self, l, h, r):
        self.left = l
        self.right = r
        self.height = h

    @property
    def line(self):
        return (self.left, self.height, self.right)

    def __repr__(self):
        return str(self.line)

    def contain_left(self, another):
        return self.left <= another.left < self.right

    def contain_right(self, another):
        return self.left < another.right <= self.right

    def parallel_to(self, another):
        return self.height == another.height


class SkyLine(object):
    def __init__(self, building):
        self.buildings = [building]

    def __str__(self):
        return str([one.line for one in self.buildings])

    def add_building(self, new_building):
        begin_building = None
        end_building = None
        begin_index = -1
        self.end_index = None
        for i, building in enumerate(self.buildings):
            if building.contain_left(new_building):
                begin_building = building
                begin_index = i
                break
        for i, building in enumerate(self.buildings):
            if building.contain_right(new_building):
                end_building = building
                self.end_index = i
                break
        '''
        '''
        import pudb
        pudb.set_trace()
        if (begin_building or end_building) is None:
            self.insert(new_building)
            return
        for one in self.buildings[begin_index + 1: self.end_index]:
            if one.height < new_building.height:
                one.height = new_building.height
        if begin_index == self.end_index:
            self.merge_middle(begin_index, begin_building, new_building)
        else:
            self.merge_begin(begin_index, begin_building, new_building)
            self.merge_end(end_building, new_building)

    def insert(self, new_building):
        left = self.buildings[0].left
        right = self.buildings[-1].right
        if new_building.right < left:
            empty = Building(new_building.right, 0, left)
            self.buildings.insert(0, empty)
            self.buildings.insert(0, new_building)
        elif new_building.left > right:
            empty = Building(right, 0, new_building.left)
            self.buildings.append(empty)
            self.buildings.append(new_building)
        elif new_building.right == left:
            self.buildings.insert(0, new_building)
        elif new_building.left == right:
            self.buildings.append(new_building)
        elif new_building.left < left and new_building.right > right:
            for building in self.buildings:
                if building.height < new_building.height:
                    building.height = new_building.height
            temp = Building(
                new_building.left,
                new_building.height,
                left,
            )
            self.buildings.insert(0, temp)
            new_building.left = right
            self.buildings.append(new_building)

    def merge_middle(self, begin_index, begin_building, new_building):
        if begin_building.height < new_building.height:
            self.buildings.insert(begin_index + 1, new_building)
            if new_building.right < begin_building.right:
                temp = Building(
                    new_building.right,
                    begin_building.height,
                    begin_building.right,
                )
                self.buildings.insert(begin_index + 2, temp)
            if begin_building.left < new_building.left:
                begin_building.right = new_building.left
            else:
                self.buildings.pop(begin_index)

    def merge_begin(self, begin_index, begin_building, new_building):
        if begin_building:
            if begin_building.height < new_building.height:
                if begin_building.left < new_building.left:
                    temp = Building(
                        new_building.left,
                        new_building.height,
                        begin_building.right,
                    )
                    self.buildings.insert(begin_index + 1, temp)
                    if self.end_index is not None:
                        self.end_index += 1
                    begin_building.right = new_building.left
                else:
                    begin_building.height = new_building.height
        else:
            temp = Building(
                new_building.left,
                new_building.height,
                self.buildings[0].left,
            )
            self.buildings.insert(0, temp)
            if self.end_index is not None:
                self.end_index += 1

    def merge_end(self, end_building, new_building):
        if end_building:
            if end_building.height < new_building.height:
                if end_building.right > new_building.right:
                    temp = Building(
                        end_building.left,
                        new_building.height,
                        new_building.right,
                    )
                    self.buildings.insert(self.end_index, temp)
                    end_building.left = new_building.right
                else:
                    end_building.height = new_building.height
        else:
            temp = Building(
                self.buildings[-1].right,
                new_building.height,
                new_building.right,
            )
            self.buildings.append(temp)

    def get_sky_line(self):
        previous = self.buildings.pop(0)
        sky_line = [previous.left, previous.height]
        building = None
        while self.buildings:
            building = self.buildings.pop(0)
            if previous.parallel_to(building):
                continue
            else:
                sky_line += [building.left, building.height]
            previous = building
        building = building or previous
        sky_line += [building.right, 0]
        sky_line = list(map(str, sky_line))
        return ' '.join(sky_line)


def to_buildings(one):
    buildings = []
    for building in one:
        line = list(map(int, re.findall(r'\d+', building)))
        building = Building(*line)
        buildings.append(building)
    return buildings


def to_sky_line(buildings):
    building = buildings.pop(0)
    sky_line = SkyLine(building)
    while buildings:
        building = buildings.pop(0)
        sky_line.add_building(building)
        #sky_line.print_buildings()
    return sky_line.get_sky_line()


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        #if one.startswith('#'):
        #    continue
        buildings = to_buildings(one.split(';'))
        print(to_sky_line(buildings))
f.close()
