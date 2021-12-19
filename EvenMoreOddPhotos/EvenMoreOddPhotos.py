n = int(input())
cowIDs = list(map(int, input().split()))

numberOfOddCows = 0
numberOfEvenCows = 0

for cowID in cowIDs:
    if cowID % 2 == 0:
        numberOfEvenCows += 1
    else:
        numberOfOddCows += 1

# Since there can't be more odd cows than even, keep putting two odd cows into one group 
# and add one to even cows since two odd cows are the same thing as one even
while numberOfOddCows > numberOfEvenCows:
    numberOfEvenCows +=1
    numberOfOddCows -= 2

# If there are too many even cows, just force all of them into one group
# since even + even is still even
if numberOfEvenCows > numberOfOddCows + 1:
    numberOfEvenCows = numberOfOddCows + 1


print(numberOfOddCows+numberOfEvenCows)
