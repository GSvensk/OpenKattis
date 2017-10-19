#Solution is too slow for kattis.


def solve(operations):
    #Superset of all sets
    allsets = set()

    for q in range(0, operations):
        inputarray = input().split()

        a = frozenset(inputarray[1])
        b = frozenset(inputarray[2])

        for j in allsets:
            #Check if a is a proper subset of any of the sets
            if a < j:
                a = j
            #Check if b is a proper subset of any of the sets
            if b < j:
                b = j

        #Handle query
        if inputarray[0] == '?':
            if a != b:
                print('no')
            else:
                print('yes')
        #Unite sets
        else:
            allsets.add(frozenset(a|b))

if __name__ == "__main__":
    tmp = input().split()
    #Send number of operations to solver
    solve(int(tmp[1]))


