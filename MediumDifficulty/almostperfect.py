import sys
import math

for line in sys.stdin:
    d = int(line)
    sum_of_divisors = 1
    counter = 2
    limit = math.sqrt(d)

    while counter < limit:
        if d % counter == 0:
            sum_of_divisors += counter
            sum_of_divisors += int(d/counter)

        counter += 1

    if int(limit)**2 == d:
        sum_of_divisors += limit

    if sum_of_divisors == d:
        print("{} perfect".format(d))
    elif abs(sum_of_divisors-d) < 3:
        print("{} almost perfect".format(d))
    else:
        print("{} not perfect".format(d))
