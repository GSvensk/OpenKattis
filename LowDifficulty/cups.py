
class Cup:

    def __init__(self, color, size):
        self.color = color
        self.size = size


cases = int(input())
cups = []

for i in range(cases):
    tmp = input().split()

    if tmp[0].isnumeric():
        cups.append(Cup(tmp[1], float(tmp[0])/2))
    else:
        cups.append(Cup(tmp[0], float(tmp[1])))

cups.sort(key=(lambda x: x.size))
list(map((lambda x: print(x.color)), cups))
