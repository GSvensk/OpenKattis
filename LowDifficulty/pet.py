maxi = -1
index = 0

for i in range(5):

    score = 0
    tmp = input().split()
    score = sum(map(int, tmp))

    if score > maxi:
        maxi = score
        index = i+1

print("{} {}".format(index, maxi))
