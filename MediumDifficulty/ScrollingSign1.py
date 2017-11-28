
cases = int(input())

for i in range(cases):
    answer = []
    # 0 = word length, 1 = number of words
    tmp = input().split()

    for j in range(int(tmp[1])):
        answer.append(input())

    # Iterate through list comparing "abc" to "def", "bc" to "de" and "c" to "d"
    for k in range(len(answer)-1):
        for j in range(len(answer[k])):
            if answer[k][j:len(answer[k])] == answer[k+1][0:len(answer[k])-j]:
                answer[k] = answer[k][0:j]

    # Turn list into string
    answer = ''.join(map(str, answer))
    print(len(answer))
