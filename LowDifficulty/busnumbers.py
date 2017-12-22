def make_chain(bus_lines, total_buses, counter):
    print(bus_lines[counter], end="")
    while counter+2 < total_buses:
        if (bus_lines[counter+1] == bus_lines[counter]+1) & (bus_lines[counter+2] == bus_lines[counter]+2):
            counter += 1
        else:
            break

    print("-" + str(bus_lines[counter+1]) + " ", end="")
    return counter+2


buses = int(input())
bus_numbers = list(map(int, input().split()))
bus_numbers.sort()
k = 0

while k < buses-2:
    if (bus_numbers[k+1] == bus_numbers[k] + 1) & (bus_numbers[k+2] == bus_numbers[k] + 2):
        k = make_chain(bus_numbers, buses, k)
    else:
        print(str(bus_numbers[k]) + " ", end="")
        k += 1

while k < buses:
    print(str(bus_numbers[k]) + " ", end="")
    k += 1
