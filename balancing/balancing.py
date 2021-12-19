with open('balancing.in') as f:
    lines = [list(map(int, l.strip('\n').split(' '))) for l in f.readlines()]

n = lines[0][0]
lines = lines[1:]


def m(lx, ly):
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0

    for cow in lines:
        x = cow[0]
        y = cow[1]

        assert x != lx and y != ly
        assert lx % 2 == 0 and ly % 2 == 0

        if x > lx and y > ly:
            q1 += 1

        elif x < lx and y > ly:
            q4 += 1

        elif x < lx and y < ly:
            q3 += 1

        elif x > lx and y < ly:
            q2 += 1

    # Return max of the four quadrants as m
    return max(q1, q2, q3, q4)


lm = n

xCords = []
yCords = []
for cow in lines:
    xCords.append(cow[0] + 1)
    yCords.append(cow[1] + 1)

for x in xCords:
    for y in yCords:
        lm = min(lm, m(x, y))

with open('balancing.out', 'w+') as f:
    f.write(str(lm) + '\n')
