
cases = int(input())

for i in range(cases):

    input()
    kids = int(input())
    total = 0

    for j in range(kids):
        total += int(input())

    if total % kids == 0:
        print("YES")
    else:
        print("NO")

