
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


def check_building(x, y):
    return not (world[x][y] == '#') | (world[x+1][y] == '#') | (world[x][y+1] == '#') | (world[x+1][y+1] == '#')


def is_car(hi):
    return world[hi.x][hi.y] == 'X'


def park_possibilities_1(x, y):
    points = [Point(x, y), Point(x+1, y), Point(x, y+1), Point(x+1, y+1)]
    return len(list(filter(is_car, points)))


coordinates = input().split()
rows = int(coordinates[0])
columns = int(int(coordinates[1]))

world = []

for i in range(rows):
    world.append(list(input()))

ans = [0 for x in range(5)]

for i in range(rows-1):
    for j in range(columns-1):
        if check_building(i, j):
            ans[park_possibilities_1(i, j)] += 1

for i in range(len(ans)):
    print(ans[i])

