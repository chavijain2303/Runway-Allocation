import heap
import random
def assign(data):
    for a in data:
        if a[0] == "diplomatic":
            a[0] = 7500 + random.randint(1, 1000)

        elif a[0] == "private":
            a[0] = 6000 + random.randint(1, 1000)

        elif a[0] == "international":
            a[0] = 4500 + random.randint(1, 1000)

        elif a[0] == "domestic":
            a[0] = 3000 + random.randint(1, 1000)

        elif a[0] == "cargo":
            a[0] = 1500 + random.randint(1, 1000)

    heap.heapify(data)