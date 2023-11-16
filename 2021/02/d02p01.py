depth = 0
position = 0
with open("d02p01.input", "r") as f:
    for line in f:
        action=line.split(" ")[0];
        if action == 'forward':
            position = position + int(line.split(" ")[1])
        elif action == 'up':
            depth = depth - int(line.split(" ")[1])
        elif action == 'down':
            depth = depth + int(line.split(" ")[1])
        else:
            print("Unknown action: " + action)
    pass
pass
print(depth)
print(position)
print (depth * position)
