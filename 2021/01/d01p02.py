totalIncreases = 0
previousSum = "A";

with open("d01p01.input", "r") as f:
    lines = f.readlines()
    for i, current in enumerate(lines):
        if i >= 2:
            currentSum = int(lines[i].strip()) + int(lines[i - 1].strip()) + int(lines[i - 2].strip())
            if previousSum != "A":
                if int(previousSum) < int(currentSum):
                    totalIncreases += 1
                pass
            pass
            previousSum = currentSum
            currentSum = 0
        pass
    pass
pass
print(totalIncreases)
