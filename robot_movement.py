total = 0
temp = [[(0,0)]]

n = 4
def go_to(point, a, b):
    a = point[0]+a
    b = point[1]+b
    if -1 < a < n and -1 < b < n:
        return (a, b)

four = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def go_next(route):
    routes = []
    last = route[-1]
    for one in four:
        p = go_to(last, *one)
        if p:
            routes.append(route + [p])
    return routes

while temp:
    ans = []
    for route in temp:
        routes = go_next(route)
        for i, route in enumerate(routes):
            if len(route) != len(set(route)):
                routes[i] = None
                continue
            if route[-1] == (n-1, n-1):
                routes[i] = None
                total += 1
        routes = filter(None, routes)
        ans.extend(routes)
    temp = ans 

print total
