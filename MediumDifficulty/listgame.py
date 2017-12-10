
x = int(input())
ans = 0
div = 3

while (x % 2) == 0:
    ans += 1
    x //= 2

while div * div <= x:
    while (x % div) == 0:
        ans += 1
        x //= div
    div += 2
if x > 1:
    ans += 1

print(ans)