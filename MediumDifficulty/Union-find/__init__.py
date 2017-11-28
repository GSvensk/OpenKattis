
class Node:

    def __init__(self, nummer):
        self.nummer = int(nummer)
        self.friends = set()

    def merge(self, b):
        #self.friends = self.friends.union(b.get_friends())
        self.friends = self.friends|b.friends
        b.friends = self.friends
        self.friends.add(b)
        b.friends.add(self)

    def friends_with(self, b):
        return b in self.friends

    def print_friends(self):
        print("node: {}".format(self.nummer))
        for i in self.friends:
            print(i.nummer)

tmp = input().split()
noofelements = int(tmp[0])
operations = int(tmp[1])
nodes = []
numbers = set()

for i in range(0, operations):
    tmp = input().split()
    query = tmp[0]

    if int(tmp[1]) in numbers:
        for j in nodes:
            if j.nummer == int(tmp[1]):
                a = j
    else:
        numbers.add(int(tmp[1]))
        a = Node(int(tmp[1]))
        nodes.append(a)

    if int(tmp[2]) in numbers:
        for k in nodes:
            if k.nummer == int(tmp[2]):
                b = k
    else:
        numbers.add(int(tmp[2]))
        b = Node(int(tmp[2]))
        nodes.append(b)

    if query == '?':
        if a.friends_with(b):
            print('yes')
        elif b.friends_with(a):
          print('yes')
        elif a == b:
            print('yes')
        else:
            print('no')
    else:
        #a.add_friend(b)
        #b.add_friend(a)
        a.merge(b)
