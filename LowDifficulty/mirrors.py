
cases = int(input())

for i in range(cases):
    tmp = input().split()
    rows = int(tmp[0])
    columns = int(tmp[1])

    matrix = [[0 for x in range(columns)] for y in range(rows)]

    for j in range(rows):
        matrix[j] = list(input())

    print("Test {}".format(i+1))
    for x in reversed(range(rows)):
        print("".join(reversed(matrix[x])))