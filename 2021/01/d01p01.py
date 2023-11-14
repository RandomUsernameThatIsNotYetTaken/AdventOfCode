totalIncreases = 0
previous = "A";
with open("d01p01.input", "r") as f:
    for current in f:
        if previous != "A":
            if int(previous) < int(current):
                totalIncreases += 1
        pass
        previous = current
    pass
pass
print(totalIncreases)
