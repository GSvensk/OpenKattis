
text = list(input())

answer = []
counter = 0

while counter < len(text):

    if text[counter] != '<':
        answer.append(text[counter])
    else:
        answer.pop()

    counter += 1

print(''.join(answer))
