
names = int(input())
list_of_names = []

for i in range(names):
    list_of_names.append(input())

cpy = list_of_names.copy()
list_of_names.sort()

if cpy == list_of_names:
    print('INCREASING')
else:
    list_of_names.sort(reverse=True)
    if list_of_names == cpy:
        print('DECREASING')
    else:
        print('NEITHER')