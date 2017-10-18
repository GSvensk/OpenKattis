
class Node:

    def __init__(self, nummer):
        self.nummer = nummer
        self.friends = []

    def printing(self):
        print(self.nummer)

        #str = self.friends.copy()
        #print('friends: ')
        #for i in str:
           # str.pop().printing()


    def add_friend(self, friend):
        self.friends += friend.get_friends()
        self.friends.append(friend)

    def get_friends(self):
        return self.friends

    def friends_with(self, b):
        return (b in self.friends)


def solve():
    tmp = input().split()
    noofelements = int(tmp[0])
    operations = int(tmp[1])
    nodes = []

    for i in range(0, noofelements):
        nodes.append(Node(i))

    for i in range(0, operations):
        tmp = input().split()
        query = tmp[0]

        a = nodes[int(tmp[1])]
        b = nodes[int(tmp[2])]

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
            a.add_friend(b)
            b.add_friend(a)


if __name__ == '__main__':
    solve()
