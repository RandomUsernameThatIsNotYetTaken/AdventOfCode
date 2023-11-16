def checkNumbers(number, puzzle):
    for row in puzzle:
        for i in range(len(row)):
            if row[i] == number: 
                row[i] = 'X'
           #     print("Found ", number, " in ", puzzle)
    return puzzle    


def checkBingo(puzzle):
    for row in puzzle:
        if row.count('X') == 5:
            print("Bingo in row: ", row	)
            return True
    puzzle_transposed=list(map(list,zip(*puzzle) ))
    for column in puzzle_transposed:
        if column.count('X') == 5:
            print("Bingo in column: ", column	)
            return True
    return False

def countBingo(puzzle):
    count = 0
    for row in puzzle:
        for i in range(len(row)):
            if row[i] != 'X': 
                count = count+int(row[i])
    return count

with open("d04p01.input", "r") as f:
    content = f.readlines()
    drawnNumbers=content[0].split(",")
    puzzlesRaw = content[2:]
    puzzlesCleaned1 = list(line.split() for line in puzzlesRaw)
    puzzlesCleaned = [puzzlesCleaned1[x:x+5] for x in range(0, len(puzzlesCleaned1), 6)]
    
    bingoFound = False
    for drawnNumber in drawnNumbers:
        for puzzle in puzzlesCleaned:
            puzzle = checkNumbers(drawnNumber, puzzle)
            if checkBingo(puzzle) == True:
                bingoFound = True
                print("Bingo!")
                print(puzzle)
                bingoPuzzle = puzzle
                count = countBingo(bingoPuzzle);
                winningNumber = drawnNumber
                break
        if bingoFound == True:
            break
print("Winning Number: ", winningNumber)
print("Count: ", count)
print(count*int(winningNumber))