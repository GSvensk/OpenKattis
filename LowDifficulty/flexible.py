
tmp = list(map(int, input().split()))
w = tmp[0]
p = tmp[1]

combinations = list(map(int, input().split()))
combinations.append(w)
answer = list(combinations)

# highest number minus 2nd highest number, highest minus 3rd highest etc.
# 2nd highest number minus 3rd highest, 2nd highest minus 4th highest etc.
# 2nd lowest number minus lowest.
for i in range(p+1):
    for j in range(p+1-i):
        answer.append((combinations[p-i]-combinations[p-i-j]))

# remove duplicates
answer = list(set(answer))
# remove elements less than 1
answer = list(filter(lambda x: x > 0, answer))
answer.sort()

for i in range(len(answer)):
    print(answer[i], end=" ")
