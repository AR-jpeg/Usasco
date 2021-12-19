with open('pails.in') as f:
    lines = f.read()

lines = lines.split(' ')

x = int(lines[0])
y = int(lines[1])
m = int(lines[2])


maximumToFill = 0


for i in range(0, int(m/x)+1):
    for k in range(0, (int(m/x) + 1 - i)):
        possibleMilk = (i*x) + (k*y)

        if possibleMilk <= m:
            maximumToFill = max(maximumToFill, possibleMilk)

# while True:
#     maximumToFill += x

#     print(maximumToFill)
#     if maximumToFill > m:
#         maximumToFill -= x
#         break

# while True:
#     if ((maximumToFill - x) + y) > maximumToFill and ((maximumToFill - x) + y) <= m:
#         maximumToFill -= x
#         maximumToFill += y
#     # We already have max
#     else:
#         break


"""

loop "i" 0 - m/x
    loop "k" 0 - m/y
        possibleMilk := (i*x) + (k*y)

    if possibleMilk > currentMaxMilk
        currentMaxMilk := possibleMilk

"""

with open('pails.out', 'w') as f:
    f.write(str(maximumToFill))
