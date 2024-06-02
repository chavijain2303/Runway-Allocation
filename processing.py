from avltree import *

def allocation(data):
    runways = []
    unavailable = []
    tester = 1
    for i in range(1, 6):
        runways.append(AVL())
    for flight in data:
        i = 0
        for runway in runways:
            i = i + 1
            if runway.canBeInserted(flight):
                runway.insert(flight)
                tester = 0
                flight.append(i)
                break

        if tester == 1:
            unavailable.append(flight)
            flight.append("Not Allocated")