
p = int(input())

for i in range(0, p):
    arr = input().split()
    a = int(arr[1])

    plusone = int((a**2 + a)/2)

    print("{} {} {} {}".format(arr[0], plusone, 2*plusone - int(arr[1]), 2*plusone))