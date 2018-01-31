
x = int(input())
ans = 0
div = 3
same = 2

while x % same:
    ans +=1
    x //= same
    same = same*same

while div * div <= x:
    if (x % div) == 0:
        print("x: {} div: {} res: {}".format(x, div, x / div))
        x //= div
        same = div * div
        while (x % same) == 0:
            ans += 1
            same = div*div
            x //= same
    div += 2
if x > 1:
    ans += 1

print(ans)