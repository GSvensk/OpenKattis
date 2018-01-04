
input()

rolls = list(map(int, input().split()))
winner = False
highest_roll = 6

while highest_roll != 0:
    if rolls.count(highest_roll) == 1:
        print(rolls.index(highest_roll)+1)
        winner = True
        break
    else:
        highest_roll -= 1

if not winner:
    print('none')