with open('cowsignal.in') as f:
    lines = [s.strip('\n').split() for s in f.readlines()]

k = int(lines[0][2])
lines = lines[1:]

res = []

for i in range(len(lines)):
    line = ""

    for char in lines[i][0]:
        line += (char * k)

    for j in range(k):
        res.append(line)


for line in lines:
    print(line)
print()

for line in res:
    print(line)


with open('cowsignal.out', 'w+') as f:
    for line in res:
        f.write(line + "\n")
