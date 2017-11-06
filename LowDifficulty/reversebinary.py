# "{0:b}".format(n) turns n into binary, n[::-1] reverses n
# and int(n,2) turns n into base 10 from binary
print(int("{0:b}".format(int(input()))[::-1], 2))
