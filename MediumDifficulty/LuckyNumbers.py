import math

summa = 0

divisible = True

for x in range(2, 14):
    start = math.pow(10, x - 1)
    end = math.pow(10, x) - 1

    for j in range(int(start), int(end)):
        for k in range(2, (x+1)):
            if float(str(j)[:k]) % k != 0:
                divisible = False

        if divisible:
            summa += 1

        divisible = True

    print(summa)
    summa = 0
