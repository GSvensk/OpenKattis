import math


def complexity(n, t, maxi):
    # factorial
    if t == 1:
        ans = 1
        k = 2
        if n == 1:
            return True

        while (ans <= maxi) & (k < n):
            ans = ans * k
            k += 1

        ans = ans*k
        return (k == n) & (maxi >= ans)

    # 2^n
    elif t == 2:
        ans = 1
        k = 1
        if (maxi > 1) & (n == 1):
            return True

        while (k < n) & (ans <= maxi):
            ans *= 2
            k += 1

        ans = ans * 2
        return (k == n) & (maxi >= ans)

    elif t == 3:
        return n ** 4 <= maxi
    elif t == 4:
        return n ** 3 <= maxi
    elif t == 5:
        return n ** 2 <= maxi
    elif t == 6:
        return (n * math.log(n, 2)) <= maxi
    elif t == 7:
        return n <= maxi


tmp = list(map(int, input().split()))
m = tmp[0]

if complexity(tmp[1], tmp[2], m):
    print("AC")
else:
    print("TLE")
