
input()
# save input as list of integers
days = list(map(int, input().split()))
day = 1
answer = 1

days.sort()

while days:
    # time it takes for the slowest tree + current day
    a = days.pop() + day
    if a > answer:
        answer = a

    day += 1

print(answer+1)