
#split string input into 2 parts
tmp = input().split()
rooms = int(tmp [0])
noOfBooked = int(tmp [1])

#create list from 1 to number of rooms+1
availableRooms = list(range(1,rooms+1))

#remove booked rooms from available rooms
for i in range(0, noOfBooked):
    tmp = int(input())
    if tmp in availableRooms:
        availableRooms.remove(tmp)

#print result
if rooms == noOfBooked:
    print("too late")
else:
    print(availableRooms.pop(0))
