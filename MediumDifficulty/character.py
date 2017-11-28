import math

n = int(input())
answer = 0

if n < 2:
    print(answer)
else:
    for i in range(2, n):
        answer = answer + (math.factorial(n)/(math.factorial(i)*(math.factorial(n-i))))

    answer += 1
    s = '{0:f}'.format(answer)
    print(s[0:s.index('.')])