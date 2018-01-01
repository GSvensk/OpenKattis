import sys

counter = 1

for line in sys.stdin:
    line = list(map(int, line.split()))
    mini = min(line[1:])
    maxi = max(line[1:])
    print("Case {}: {} {} {}".format(counter, mini, maxi, maxi-mini))
    counter += 1