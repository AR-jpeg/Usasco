with open('cbarn.in') as f:
    lines = [int(l.strip('\n')) for l in f.readlines()]

n = lines[0]
lines = lines[1:]

print(lines)

cowsInEachCell = []

for line in lines:
    cowsInEachCell.append(line)

ans = n * n * 100

for i in range(n):
    distance = 0  # The distance if you open the cell at `i`

    for k in range(n):  # The amount we need to add to cover al the cells,
        # but there is a problem since tthe array is a circle so wee need to `loop around` So we use the modulo against the current index

        #
        distance += k * cowsInEachCell[(i+k) % n]

    if distance < ans:
        ans = distance

with open('cbarn.out', 'w') as f:
    f.write(str(ans) + '\n')
