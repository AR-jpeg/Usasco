"""
Problem Stuck in a Rut
USACO Competition December, 2020
This problem took me  minutes, and  seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""

n = int(input())
cows = []

inf = float('inf')

for i in range(n):
    cows.append(input().split())
    cows[i].append(inf)
    cows[i][1] = int(cows[i][1])
    cows[i][2] = int(cows[i][2])


def getIntersection(cow, comparingTo):
    """Returns the time it takes for both cow and comparingTo takes to get to the closest intersection. cow[0] is the direction it it going"""

    if cow[0] == comparingTo[0]:  # Both facing East, or North
        return (inf, inf)

    if cow[0] == "N" and comparingTo[0] == "E":
        # If cow is below comparingTo, and to the right of comparingTo
        if cow[1] > comparingTo[1] and comparingTo[2] > cow[2]:
            timeForComparingToIntersection = cow[1] - comparingTo[1]
            timeForCowToIntersection = comparingTo[2] - cow[2]

            if timeForComparingToIntersection < timeForCowToIntersection:
                return (timeForCowToIntersection, inf)
            elif timeForCowToIntersection == timeForComparingToIntersection:
                return (timeForCowToIntersection, timeForComparingToIntersection)
            else:
                return (inf, timeForComparingToIntersection)

        else:
            return (inf, inf)

    else:
        # If cow is abouve comparingTo, and to the left of comparingTo
        if cow[1] < comparingTo[1] and comparingTo[2] < cow[2]:
            timeForCowToIntersection = comparingTo[1]-cow[1]
            timeForComparingToIntersection = cow[2]-comparingTo[2]

            if timeForComparingToIntersection < timeForCowToIntersection:
                return (timeForCowToIntersection, inf)
            elif timeForCowToIntersection == timeForComparingToIntersection:
                return (timeForCowToIntersection, timeForComparingToIntersection)
            else:
                return (inf, timeForComparingToIntersection)

        else:
            return (inf, inf)


for cow in cows:
    for cComparing in cows:
        if cow == cComparing:
            continue

        # In the format: cow takes x seconds to get there, while cComparing takes y seconds to get there
        timeToGetToIntersection = getIntersection(cow, cComparing)

        print(timeToGetToIntersection)
        """
        Only update cow[4] if the other cow has not already been stopped; if the other cows' cow[4] is less than intersection
        """

        # This one is cow                 This one is cCow
        if timeToGetToIntersection[0] > timeToGetToIntersection[1]:
            cow[3] = min(cow[3], timeToGetToIntersection[0])

        if timeToGetToIntersection[1] > timeToGetToIntersection[0]:
            cComparing[3] = min(cComparing[3], timeToGetToIntersection[1])


for cow in cows:
    print(cow[3])
