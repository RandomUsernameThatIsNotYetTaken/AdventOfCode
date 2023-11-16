from collections import Counter
epsilon = []
gamma = []
with open("d03p01.input", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    transposed = list(map(list, zip(*lines)))
    for row in transposed:
        line = ''.join(row)
        most_common_char = Counter(line).most_common(1)[0]
        least_common_char = Counter(line).most_common()[-1]
        gamma.append(most_common_char[0])
        epsilon.append(least_common_char[0])
    pass
pass
gamma = int(''.join(gamma), 2)
epsilon = int(''.join(epsilon), 2)
print(gamma*epsilon)