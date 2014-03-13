from sys import argv

matrix = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E'],
]


def find_all(c):
    temp = []
    for i, row in enumerate(matrix):
        for j, char in enumerate(row):
            if char == c:
                temp.append((i, j))
    return temp


def is_ajacent(last, coordinate):
    a, b = last
    c, d = coordinate
    if a == c:
        return abs(b - d) == 1
    if b == d:
        return abs(a - c) == 1


def add_one_coordinate(route, coordinate):
    last = route[-1]
    if coordinate in route[:-1]:
        return False
    elif is_ajacent(last, coordinate):
        return route + [coordinate]


def is_word_in_matrix(one):
    routes = []
    for c in one:
        coordinates = find_all(c)
        if not coordinates:
            return False
        if not routes:
            for coordinate in coordinates:
                routes.append([coordinate])
        else:
            new_routes = []
            for route in routes:
                for coordinate in coordinates:
                    new_sub_route = add_one_coordinate(route, coordinate)
                    if new_sub_route:
                        new_routes.append(new_sub_route)
            if new_routes:
                routes = new_routes
            else:
                return False
    return True


f = open(argv[1], 'r')
for one in f:
    one = one.strip()
    if one:
        print is_word_in_matrix(one)
f.close()
