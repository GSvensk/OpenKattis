class Producer:
    def __init__(self, strg):
        strg = strg.split()
        self.price = int(strg[0])
        self.start_day = int(strg[1])
        self.score = self.price + self.start_day


class Consumer:
    def __init__(self, strg):
        strg = strg.split()
        self.buy = int(strg[0])
        self.end_day = int(strg[1])
        self.score = self.buy + self.end_day

    def compare(self, prod):
        if (self.buy - prod.price > 0) & (self.end_day - prod.start_day > 0):
            return (self.buy - prod.price)*(self.end_day - prod.start_day)
        else:
            return 0


def solve(producers, consumers):
    prods = []
    cons = []

    add_p = prods.append
    for i in range(0, producers):
        add_p(Producer(input()))

    prods = sorted(prods, key=lambda producer: producer.score)
    # reduce list length if too long
    if producers > 25:
        del prods[int(-producers*0.95)]

    add_c = cons.append
    for j in range(0, consumers):
        add_c(Consumer(input()))

    cons = sorted(cons, key=lambda consumer: consumer.score, reverse=True)
    # reduce list length if too long
    if consumers > 25:
        del cons[int(-consumers*0.95)]

    profits = []

    for k in prods:
        profits.append(max(list(map(lambda x: x.compare(k), cons))))

    print(max(profits))


if __name__ == "__main__":
    tmp = input().split()
    solve(int(tmp[0]), int(tmp[1]))
