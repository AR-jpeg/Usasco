with open('angry.in') as f:
    lines = list(map(int, [l.strip('\n') for l in f.readlines()]))

nums = sorted(lines[1:])
scores = []  # In the notation of [(pos, score)]

print(nums)
print("\n"*100)


def getBlasts(t: int, n: int, blasts: int, dir: int) -> int:
    if dir == -1:
        print("GOING LEFT FOR " + str(n))
        # Nothing left to blast toward the left, just return the total so far
        if nums.index(n) == 0:
            print("YESSSS " + str(n))
            return blasts

        if n - nums[nums.index(n)-1] < t:
            return blasts+1

        for temp in nums:
            if n-temp <= t:
                furthestBlast: int = temp
                distanceBetweenFurthestBaleAndN = len(
                    nums[nums.index(temp):nums.index(n)])

                # We added all the blocks we could since we are going from the bottom up
                blasts += distanceBetweenFurthestBaleAndN

                break

    if dir == 1:
        print("GOING RIGHT FOR " + str(n))

        if nums.index(n) == len(nums)-1:
            print('RIGHT IS OVER FOR ' + str(n))
            return blasts

        # Nothing left to blast toward the right, just return the total so far
        if nums[nums.index(n)+1] - n > t:
            return blasts

        for temp in list(reversed(nums)):
            if temp-n <= t and temp >= t:
                furthestBlast: int = temp
                # Switch nums.index(temp) and nums.index(n) since temp is going to be bigger than n
                distanceBetweenFurthestBaleAndN = len(
                    nums[nums.index(n):nums.index(temp)])

                # We added all the blocks we could since we are going from the bottom up
                blasts += distanceBetweenFurthestBaleAndN

                break

    return getBlasts(t+1, furthestBlast, blasts, dir)


for num in nums:
    score = 0
    score += getBlasts(1, num, 0, -1)
    print("FINSIHED LEFT MOVING ON TO RIGHT FOR " + str(num))
    score += getBlasts(1, num, 0, 1)

    score += 1

    scores.append((nums.index(num), score))


maxScore = max(scores, key=lambda x: x[1])

print(scores[11])

with open('angry.out', 'w') as f:
    f.write(str(maxScore[1]) + "\n")
