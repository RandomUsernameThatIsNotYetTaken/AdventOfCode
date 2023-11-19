    
def parseLine(line):
    arr = line.split()
    x1 = int(arr[0].split(",")[0])
    y1 = int(arr[0].split(",")[1])
    x2 = int(arr[2].split(",")[0])
    y2 = int(arr[2].split(",")[1])
    return (x1, y1, x2, y2)

def findHighestX(lines):
    hightestX = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if int(x2) > hightestX:
            hightestX = int(x2)
        if int(x1) > hightestX:
            hightestX = int(x1)
    return hightestX

def findHighestY(lines):
    hightestY = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if int(y2) > hightestY:
            hightestY = int(y2)
        if int(y1) > hightestY:
            hightestY = int(y1)
    return hightestY

def createGrid(x, y):
    grid = []
    for i in range(x+1):
        grid.append([])
        for j in range(y+1):
            grid[i].append(0)
    return grid

def printGrid(grid):
    grid_transposed=list(map(list,zip(*grid) ))
    for row in grid_transposed:
        strRow = [str(i) for i in row]
        print(''.join(strRow))

def drawLine(grid, line):
    x1, y1, x2, y2 = line
    if(x1 == x2 ):
        if y1 < y2:
            Y_incr = 1
            yMin = y1
            yMax = y2+1
        else:
            Y_incr = -1
            yMin = y1
            yMax = y2-1
        print("Drawing Vertical line [x1,y1,x2,y2]: ", line, Y_incr)
        (X, Y) = (x1, yMin)
        while True:
            print("grid[x1][Y] = ", x1,Y)
            grid[x1][Y] += 1
            Y += Y_incr
            if (Y) == (yMax):
                return grid 
    if(y1 == y2):
        if x1 < x2:
            X_incr = 1
            xMin = x1
            xMax = x2+1
        else:
            X_incr = -1
            xMin = x1
            xMax = x2-1
        print("Drawing Horizontal line [x1,y1,x2,y2]: ", line, X_incr)
        (X, Y) = (xMin, y1)
        while True:
            print("grid[X][y1] = ", X,y1)
            grid[X][y1] += 1
            X += X_incr
            if (X) == (xMax):
                return grid
    else:
        if x1 < x2:
            X_incr = 1
            xMin = x1
            xMax = x2+1
        else:
            X_incr = -1
            xMin = x1
            xMax = x2-1
        if y1 < y2:
            Y_incr = 1
            yMin = y1
            yMax = y2+1
        else:
            Y_incr = -1
            yMin = y1
            yMax = y2-1
        print("Drawing Diagonal line [x1,y1,x2,y2]: ", line, X_incr, Y_incr)
        (X, Y) = (x1, y1)
        while True:
            print("grid[X][Y] = ", X,Y)
            grid[X][Y] += 1
            X += X_incr
            Y += Y_incr
            print(X,Y,xMax,yMax)
            if (X, Y) == (xMax, yMax):
                break
        return grid

def countDangerousPoints(grid,maxX,maxY):
    count = 0
    for x in range(maxX+1):
        for y in range(maxY+1):
            if grid[x][y] > 1:
                count += 1
    return count

with open("d05p01.input", "r") as f:
    content = f.readlines()
    lines = [parseLine(line) for line in content]
    maxX = findHighestX(lines)
    maxY = findHighestY(lines)
    print("Creating grid for max X and Y: ", maxX, maxY, "...")
    grid = createGrid(maxX, maxY)
    print(len(grid), len(grid[0]))
    printGrid(grid)
    print("Grid created!")
    print("Drawing lines...")
    for line in lines:
        grid = drawLine(grid, line)
    print("Lines drawn!")
    print("Printing grid...")
    printGrid(grid)
    print("Grid printed!")
    countDangerousPoints = countDangerousPoints(grid, maxX, maxY)
    print("Counting dangerous points...")
    print("Dangerous points: ", countDangerousPoints)