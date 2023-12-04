#Shitty code to find surroundingCoordinates
def getSurroundingCoordinates(number,lineNumber, bounds):
  surroundingCoordinates = []
  numberCoordinates = []
  for i in range(number[1][0],number[1][1]+1):
    numberCoordinates.append((lineNumber,i))
  for i in range(number[1][0],number[1][1]+1):
    surroundingCoordinates.append((lineNumber-1,i))
    surroundingCoordinates.append((lineNumber+1,i))
    surroundingCoordinates.append((lineNumber,i+1))
    surroundingCoordinates.append((lineNumber,i-1))
    surroundingCoordinates.append((lineNumber+1,i+1))
    surroundingCoordinates.append((lineNumber-1,i+1))
    surroundingCoordinates.append((lineNumber+1,i-1))
    surroundingCoordinates.append((lineNumber-1,i-1))
  surroundingCoordinates = set(surroundingCoordinates)
  surroundingCoordinates = surroundingCoordinates - set(numberCoordinates)
  surroundingCoordinates = list(surroundingCoordinates)
  trimmedCoordinates = surroundingCoordinates.copy()
  for coordinates in surroundingCoordinates:
    if coordinates[0] < 0 or coordinates[0] > bounds[0] or coordinates[1] < 0 or coordinates[1] > bounds[1]:
      trimmedCoordinates.remove(coordinates)
  return trimmedCoordinates

def getNumbersinRow(row):
  numbers = []
  number = '0'
  firstCoordinate = None
  lastCoordinate = None
  for i in range(0,len(row)):
    if row[i].isdigit():
      number = number+row[i]
      if firstCoordinate == None:
        firstCoordinate = i
    if (not row[i].isdigit() or i == len(row)-1) and number!= '0':
      lastCoordinate = i-1
      numbers.append((int(number),(firstCoordinate,lastCoordinate)))
      number = '0'
      firstCoordinate = None
      lastCoordinate = None
  return numbers

def getBounds(matrix):
  return (len(matrix[0])-2,len(matrix)-1)

def checkSurroundingCoordinates(matrix,coordinates, number):
  for coordinate in coordinates:
    if not matrix[coordinate[0]][coordinate[1]].isdigit() and matrix[coordinate[0]][coordinate[1]] != ".":
      return True
  return False

with open("2023_03.input", "r") as f:
  lines = f.readlines()
  matrix = [list(line) for line in lines]
  bounds = getBounds(matrix)
  lineNumber = 0
  totalp1 = 0
  totalp2 = 0
  for line in lines:
    line = list(line.strip())
    numbers = getNumbersinRow(line)
    for number in numbers:
        surroundingCoordinates = getSurroundingCoordinates(number,lineNumber, bounds)
        if checkSurroundingCoordinates(matrix,surroundingCoordinates, number):
          totalp1 += number[0]
    lineNumber += 1
print("Total p1: ",totalp1)
