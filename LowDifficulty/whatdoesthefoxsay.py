
T = int(input())

for j in range(T):
    sounds = list(input().split())
    line = input().split()

    while len(line) < 4:
        for i in range(sounds.count(line[2])):
            sounds.remove(line[2])
        line = input().split()

    print(" ".join(sounds))
