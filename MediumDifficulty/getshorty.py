import bisect
from functools import total_ordering


# Edge class
class Corridor:

    def __init__(self, end, factor):
        self.end = end
        self.factor = factor


# Node class
@total_ordering
class Intersection:

    def __init__(self, number):
        self.number = number
        self.corridors = []
        self.remaining = 0

    def add_corridor(self, corr):
        self.corridors.append(corr)

    # Needed because of bisect.insort
    def __lt__(self, other):
        return self.remaining < other.remaining


# Djikstra's Algorithm
def search(start):

    heap = [start]

    while heap:
        head = heap.pop()
        # for all corridors connecting to the intersection
        for corridor in head.corridors:
            u = corridor.end
            new = head.remaining * corridor.factor
            # update if new path is better than previous
            if new > u.remaining:
                u.remaining = new
                # heap is already sorted, just add u
                bisect.insort(heap, u)


tmp = input().split()
n = int(tmp[0])
m = int(tmp[1])

while (n != 0) & (m != 0):
    intersections = []

    # Create intersections (Nodes)
    for i in range(n):
        intersections.append(Intersection(i))

    intersections[0].remaining = 1

    # Add Corridors (Edges)
    for i in range(m):
        tmp = input().split()
        x = int(tmp[0])
        y = int(tmp[1])
        f = float(tmp[2])
        intersections[x].add_corridor((Corridor(intersections[y], f)))
        intersections[y].add_corridor((Corridor(intersections[x], f)))

    #Djikstras
    search(intersections[0])
    print("{:.4f}".format(intersections[n-1].remaining))

    tmp = input().split()
    n = int(tmp[0])
    m = int(tmp[1])
