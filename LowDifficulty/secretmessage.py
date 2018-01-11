import math

cases = int(input())

for i in range(cases):
    message = input()
    L = len(message)
    K = int(math.ceil(math.sqrt(L)))
    M = int(K**2)
    # Pad the message
    message += ("*" * (int(M-L)))

    for k in range(K):
        for j in range(1, (K+1)):
            a = int(((M+k)-j*K) % M)
            if message[a] != '*':
                print(message[a], end="")
    print()
