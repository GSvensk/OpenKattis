
winner_unis = set()
winners = 0
unis = int(input())

for i in range(unis):

    tmp = input().split()

    if winners < 12:
        if not winner_unis.__contains__(tmp[0]):
            print("{} {}".format(tmp[0], tmp[1]))
            winner_unis.add(tmp[0])
            winners += 1
        else:
            winner_unis.add(tmp[0])
