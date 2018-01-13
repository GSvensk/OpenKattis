
cases = int(input())

for i in range(cases):
    tmp = input()
    if tmp == "P=NP":
        print("skipped")
    else:
        tmp = list(tmp)
        plus = tmp.index('+')
        # print ((integer before plus character) + (integer after plus character))
        print(int("".join(tmp[0:plus])) + int("".join(tmp[plus+1:])))
