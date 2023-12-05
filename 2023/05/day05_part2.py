def getRangeBlocks(lines):
    s_to_s = parseRangeBlock(lines.split(":")[2].split("\n")[1:-2])
    s_to_f = parseRangeBlock(lines.split(":")[3].split("\n")[1:-2])
    f_to_w = parseRangeBlock(lines.split(":")[4].split("\n")[1:-2])
    w_to_l = parseRangeBlock(lines.split(":")[5].split("\n")[1:-2])
    l_to_t = parseRangeBlock(lines.split(":")[6].split("\n")[1:-2])
    t_to_h = parseRangeBlock(lines.split(":")[7].split("\n")[1:-2])
    h_to_t = parseRangeBlock(lines.split(":")[8].split("\n")[1:-2])
    return (s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_t)
    
def parseRangeBlock(rangeBlock):
    rangeBlockParsed = [ [int(x) for x in line.split(" ")] for line in rangeBlock]

    return rangeBlockParsed
    
def getSeedsRanges(lines):
    lines = lines.split("\n")[0].split(":")[1].strip().split()
    seedRanges = [tuple(lines[i:i+2]) for i in range(0, len(lines), 2)]
    print("SeedRanges: " + str(seedRanges))
    return seedRanges

def getSeeds(start,length):
    seeds = []
    for i in range(length):
        seeds.append(start+i)
    
    print("Seeds: " + str(seeds))
    return seeds

def findCorrespondingRange(input, rangeMap):
    output = input
    for range in rangeMap:
        print("input: " +  str(input))
        print("range: " + str(range))
        if input >= range[1] and input < range[1]+range[2]:
            output = range[0]+(input-range[1])
            break
    print("output: " +  str(output))
    return output



with open("2023_05.input", "r") as f:
    lines = f.read()
    seedRanges = getSeedsRanges(lines)
    locations = []
    (s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l) = getRangeBlocks(lines)
    print("Seed to Soil: " + str(s_to_s))
    print("Soil to Fertilizer: " + str(s_to_f))
    print("Fertilizer to Water: " + str(f_to_w))
    print("Water to Light: " + str(w_to_l))
    print("Light to Temperature: " + str(l_to_t))
    print("Temperature to Humidity: " + str(t_to_h))
    print("Humidity to Location: " + str(h_to_l))
    
    for seedRange in seedRanges:
        seeds = getSeeds(int(seedRange[0]),int(seedRange[1]))
        for seed in seeds:
            print("seed: " +  str(seed))
            soil = findCorrespondingRange(seed, s_to_s)
            print("seed to soil: " +  str(soil), end="\n\n")
            fertilizer = findCorrespondingRange(soil, s_to_f)
            print("soil to fertilizer: " +  str(fertilizer), end="\n\n")
            water = findCorrespondingRange(fertilizer, f_to_w)
            print("fertilizer to water: " +  str(water), end="\n\n")
            light = findCorrespondingRange(water, w_to_l)
            print("water to light: " +  str(light), end="\n\n")
            temperature = findCorrespondingRange(light, l_to_t)
            print("light to temperature: " +  str(temperature), end="\n\n")
            humidity = findCorrespondingRange(temperature, t_to_h)
            print("temperature to humidity: " +  str(humidity), end="\n\n")
            location = findCorrespondingRange(humidity, h_to_l)
            print("humidity to location: " +  str(location), end="\n\n")
            print("")
            locations.append(int(location));
    print("Locations: " + str(locations))
    print(min(locations))
    