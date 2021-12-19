"""
Problem Just Stalling
USACO Competition January, 2021
This problem took me 20 minutes, and 0 seconds to solve

Code from Aditya Rao U (ARJPEG), 2021
"""

n = int(input())

cows = list(reversed(sorted(list(map(int, input().split())))))
stalls = list(reversed(sorted(list(map(int, input().split())))))
waysToStallCows = 1


def getPossiblePlacesForCowToGo(h, s):
    ans = 0
    for stall in s:
        if stall >= h:
            ans += 1

    return ans


for cowHeight in cows:
    possiblePlacesForCowToGo = getPossiblePlacesForCowToGo(cowHeight, stalls)
    waysToStallCows *= possiblePlacesForCowToGo

    # print(cowHeight, "remaining stalls are", stalls)
    stalls.pop(0)


# print(cows, stalls)
print(waysToStallCows)
