    
def parseLine(line):
    arr = line.split()
    x1 = arr[0].split(",")[0]
    y1 = arr[0].split(",")[1]
    x2 = arr[2].split(",")[0]
    y2 = arr[2].split(",")[1]
    return (min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2))

def findHighestX(lines):
    hightestX = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if int(x2) > hightestX:
            hightestX = int(x2)
    return hightestX

def findHighestY(lines):
    hightestY = 0
    for line in lines:
        x1, y1, x2, y2 = line
        if int(y2) > hightestY:
            hightestY = int(y2)
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
        print(''.join(str(row)), end='\n')

def drawLine(grid, line):
    x1, y1, x2, y2 = line
    if(line[0] == line[2]):
    #    print("Vertical")
     #   print("Drawing line [x1,y1,x2,y2]: ", line)
        for y in range(int(line[1]), int(line[3])+1):
            grid[int(line[0])][y] += 1
        return grid 
    if(line[1] == line[3]):
      #  print("Horizontal")
      #  print("Drawing line [x1,y1,x2,y2]: ", line)
        for x in range(int(line[0]), int(line[2])+1):
            grid[x][int(line[1])] +=1
        return grid
    else:
        #print("Diagonal, Skipping")
        return grid

def countDangerousPoints(grid):
    count = 0
    for row in grid:
        for i in range(len(row)):
            if row[i] > 1: 
                count = count+1
    return count

with open("d05p01.input", "r") as f:
    content = f.readlines()
    lines = [parseLine(line) for line in content]
    maxX = findHighestX(lines)
    maxY = findHighestY(lines)
    print("Creating grid for max X and Y: ", maxX, maxY, "...")
    grid = createGrid(maxX, maxY)
    print(len(grid), len(grid[0]))
    #printGrid(grid)
 #   print("Grid created!")
 #   print("Drawing lines...")
    for line in lines:
        grid = drawLine(grid, line)
   # print("Lines drawn!")
   # print("Printing grid...")
    #printGrid(grid)
 #   print("Grid printed!")
    countDangerousPoints = countDangerousPoints(grid)
 #   print("Counting dangerous points...")
    print("Dangerous points: ", countDangerousPoints)