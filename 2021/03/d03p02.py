from collections import Counter
oxygen = []
co2 = []


<<<<<<< HEAD
def filterCo2down(array, char, position):
=======
def filterCo2down(transposed, array, char, position):
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3
    print('Filtering co2 down')
    print(array)
    print('Length: '+ str(len(array)))
    new_array = []
    for row in array:   
        line = ''.join(row)
        if str(row[position]) == str(char):
            new_array.append(line)
        else:
            pass
    print('New Array Length: '+ str(len(new_array)))
    if len(new_array) == 1:
        print('Returning new array')
<<<<<<< HEAD
=======
        print(new_array)
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3
        return new_array
    elif len(new_array) == 0:
        print('WTF')
        return 0
    else:
        transposed = list(map(list, zip(*new_array))) 
        position += 1

        print('finding new least common in position: '+ str(position+1))
        least_common_char = Counter(''.join(transposed[position])).most_common(2)
        if least_common_char[0][1] == least_common_char[1][1]:
            print('Tie')
            least_common_char = (0,1)
        else:
            least_common_char = least_common_char[-1]
        print('Least common char: '+ str(least_common_char[0]))
<<<<<<< HEAD
        return filterCo2down(new_array, least_common_char[0], position)


def filterOxygendown(array, char, position):
=======
        return filterCo2down(transposed, new_array, least_common_char[0], position)


def filterOxygendown(transposed, array, char, position):
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3
    print('Filtering oxygen down: ' + str(char) + ' ' + str(position))
    print(array)
    print('Length: '+ str(len(array)))
    new_array = []
    for row in array:   
        line = ''.join(row)
        print('Character: '+ row[position])
        if str(row[position]) == str(char):
            print('Adding line: '+ line)
            new_array.append(line)
        else:
            pass
    print('New Array Length: '+ str(len(new_array)))
    if len(new_array) == 1:
        print('Returning new array')
<<<<<<< HEAD
=======
        print(new_array)
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3
        return new_array
    elif len(new_array) == 0:
        print('WTF')
        return 0
    else:
        transposed = list(map(list, zip(*new_array))) 
        position += 1
        print('finding new most common in position: '+ str(position+1))
        most_common_char = Counter(''.join(transposed[position])).most_common(2) 
        if most_common_char[0][1] == most_common_char[1][1]:
            print('Tie')
            most_common_char = (1,1)    
        else:
            most_common_char = most_common_char[0]
        print('Most common char: '+ str(most_common_char[0]))
<<<<<<< HEAD
        return filterOxygendown(new_array, most_common_char[0], position)
=======
        return filterOxygendown(transposed, new_array, most_common_char[0], position)
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3


with open("./d03p01.input", "r") as f:
    lines = f.readlines()
    lines = list(map(lambda x: x.strip(), lines))
    transposed = list(map(list, zip(*lines)))
    most_common_char = Counter(''.join(transposed[0])).most_common(1)[0]
    least_common_char = Counter(''.join(transposed[0])).most_common()[-1]
    print('Most common char: '+ most_common_char[0])
    print('Entering filterOxygendown')
<<<<<<< HEAD
    oxygen = filterOxygendown(lines, most_common_char[0],0)
    print('Found Oxygen: '+ str(oxygen))
    print('Least common char: '+ least_common_char[0])
    print('Entering filterCo2down')
    co2 = filterCo2down(lines, least_common_char[0],0)
=======
    oxygen = filterOxygendown(transposed, lines, most_common_char[0],0)
    print('Found Oxygen: '+ str(oxygen))
    print('Least common char: '+ least_common_char[0])
    print('Entering filterCo2down')
    co2 = filterCo2down(transposed, lines, least_common_char[0],0)
>>>>>>> 682df23c0a4170bdce63dcfa5b881682b3dbc0d3
    print('Found Co2: '+ str(co2))
    print(oxygen)
    print(co2)
pass

co2 = int(''.join(co2), 2)
oxygen = int(''.join(oxygen), 2)
print(co2*oxygen)