
class Customer:

    def __init__(self, cash, time):
        self.cash = int(cash)
        self.time = int(time)


tmp = input().split()
customers = []

# Create list of customers from input
for i in range(int(tmp[0])):
    inputarray = input().split()
    customers.append(Customer(int(inputarray[0]), int(inputarray[1])))

# Sort customers based on how much time they have
customers.sort(key = (lambda x: x.time))

# The limit is either the customer with the most time or for how long the bank can stay open
limit = min({int(tmp[1]), customers[len(customers)-1].time})

answer = 0

# Start from the back of the list, where the customers with the most time are.
for i in reversed(range(0, limit+1)):
    try:
        # Pick the customer with the most cash out of those who can stay the longest
        # Throws ValueError in case the list is empty.
        a = max((list(filter((lambda x: x.time >= i), customers))), key = (lambda x: x.cash))
        answer += a.cash
        # Remove the chosen customer
        customers.remove(a)
    except ValueError:
        answer = answer

print(answer)