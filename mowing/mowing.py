with open("mowing.in") as f:
    lines = [t.strip('\n').split() for t in f.readlines()][1:]

# In the format of {"x,y":t_subCoordinate}
timesOfCoordinates = {}

t = 0
answer = -1

for point in lines:

    dir = point[0]
    timesToGoToDirection = point[1]

    # x = point[]
    # y = point[y]
    #

    for i in timesToGoToDirection:

        if f"{x},{y}" in timesOfCoordinates:
            answer = t - timesOfCoordinates[f'{x},{y}']
            break
        t += 1

        if dir == "N":
            timesOfCoordinates[f"{x},{y+1}"] = t

        if dir == "S":
            timesOfCoordinates[f"{x},{y-1}"] = t

        if dir == "E":
            timesOfCoordinates[f"{x+1},{y}"] = t

        if dir == "W":
            timesOfCoordinates[f"{x-1},{y}"] = t


print(answer)

print(lines)
