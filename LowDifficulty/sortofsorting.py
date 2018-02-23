
words = int(input())

while words != 0:
    dic = []

    for i in range(words):
        word = input()
        dic.append(word)

    dic.sort(key=(lambda x: x[0:2]))

    for j in dic:
        print(j)

    words = int(input())
    print()
