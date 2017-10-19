
class Node:

    def __init__(self, nummer):
        self.nummer = nummer
        self.subset = set()
        self.subset.add(self)

    def print_friends(self):
        print('node: {}'.format(self.nummer))
        for i in self.subset:
            print(i.nummer)


tmp = input().split()
noofelements = int(tmp[0])
operations = int(tmp[1])
allsets = set()
allnodes = []

for i in range(0, noofelements):
    allnodes.append(Node(i))

for i in range(0, operations):
    tmp = input().split()
    query = tmp[0]

    if Node(int(tmp[1])) not in allsets:
        ax = Node(tmp[1])
        allsets.add(ax)
    else:
        ax = allnodes[int(tmp[1])]

    if Node(int(tmp[2])) not in allsets:
        bx = Node(tmp[2])
        allsets.add(bx)
    else:
        bx = allnodes[int(tmp[2])]

    if query == '?':
        if bx in ax.subset:
            print('yes')
        #elif b.friends_with(a):
         #   print('yes')
        elif ax == bx:
            print('yes')
        else:
            print('no')
    else:
        c = ax.subset|bx.subset
        ax.subset = (c)
        bx.subset = (c)
        ax.print_friends()
        bx.print_friends()



