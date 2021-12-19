
with open('art.in') as f:
    grid = [l.strip('\n') for l in f.readlines()]
    n = grid[0]
    grid = grid[1:]

print(grid)

possibleAnswers = set()
allColors = []

for line in grid:
    for color in line:
        if color != '0':
            possibleAnswers.add(color)
            allColors.append(color)

def pointIn(pointX, pointY, minX, minY, maxX, maxY):
    if (pointX > minX and pointX < maxX) and (pointY > minY and pointY < maxY):
        return True
    
    return False

def dimensions(color):
    # Get min x, max x

    minX = 10
    maxX = 0

    minY = 10
    maxY = 0

    for row in grid:
        # print(row)

        if row.count(color) > 0:

            if grid.index(row) < minY:
                minY = grid.index(row)

            if grid.index(row) > maxY:
                maxY = grid.index(row)

            if row.index(color) < minX:
                minX = row.index(color)
            
            if abs(0-(list(reversed(row)).index(color))) > maxX:
                maxX = abs(0-(list(reversed(row)).index(color)))

    for row in grid:
        for point in row:
            if (point != color) and pointIn(row.index(point), grid.index(row), minX, minY, maxX, maxY):
                try:
                    possibleAnswers.remove(point)
                except KeyError:
                    pass # We already removed this solution

    return(minX, minY, maxX, maxY)

for color in allColors:
    dimensions(color)

with open('art.out', 'w') as f:
    f.write(str(len(possibleAnswers)))