"""
Problem Comfortable Cows
USACO Competition Febuary, 2021
This problem took me  minutes, and  seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""

comfortableCows = 0
numCows = int(input())
cows = []


def numberOfAdjacent(coords):
    # coords is (int, int)
    num = 0
    x, y = coords

    # print(x, y)
    # print((x-1, y) in cows)

    if (x+1, y) in cows:
        num += 1

    if (x-1, y) in cows:
        num += 1

    if (x, y+1) in cows:
        num += 1

    if (x, y-1) in cows:
        num += 1

    return num


def getNeighbors(coords):
    x, y = coords
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


for i in range(numCows):
    # TODO: Get the adj for THIS cow AND for all of the other cows

    # if THIS cow's adj = 3, then add one from comfortableCows
    # if the other cow's adj > 3, then subtract one from comfortableCows
    # if the other cow's adj = 3, then add one from comforableCows
    cow = tuple(map(int, input().split()))
    cows.append(cow)

    # print("cows", cows)
    # print("cow", cow)
    # print("adj to", cow, numberOfAdjacent(cow))

    if numberOfAdjacent(cow) == 3:
        comfortableCows += 1

    for neighbor in getNeighbors(cow):
        if numberOfAdjacent(neighbor) == 3:
            comfortableCows += 1
        elif numberOfAdjacent(neighbor) == 4:
            comfortableCows -= 1

    print(comfortableCows)
    # print()
