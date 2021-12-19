with open('promote.in') as f:
    lines = [l.strip('\n').split() for l in f.readlines()]

    for line in lines:
        print(line)
        line[0] = int(line[0])
        line[1] = int(line[1])

brBefore, brAfter = lines[0]
slBefore, slAfter = lines[1]
goBefore, goAfter = lines[2]
plBefore, plAfter = lines[3]

# Only way to get promoted to platinum from gold is if there were more people
# in platinum before the contest, and then more in platinum after the contest
goldToPlatinum = plAfter - plBefore
silverToGold = (goAfter - goBefore) + (plAfter - plBefore)
bronzeToSilver = (plAfter+goAfter+slAfter) - (plBefore+goBefore+slBefore)


with open('promote.out', 'w') as f:
    for promotion in map(str, [bronzeToSilver, silverToGold, goldToPlatinum]):
        f.write(promotion + '\n')
