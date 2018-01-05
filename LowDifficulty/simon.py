
cases = int(input())

for i in range(cases):
    tmp = input().split()
    if " ".join(tmp[0:2]) == "simon says":
        print(" ".join(tmp[2:]))
    else:
        print()
