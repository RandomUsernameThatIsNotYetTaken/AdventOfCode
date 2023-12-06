import datetime
from os import getpid
from multiprocessing import Process, Queue

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
    #print("SeedRanges: " + str(seedRanges))
    return seedRanges

def getSeeds(start,length):
    return range(start, start+length-1)

def findCorrespondingRange(input, rangeMap):
    output = input
    for range in rangeMap:
        #print("input: " +  str(input))
        #print("range: " + str(range))
        if input >= range[1] and input < range[1]+range[2]:
            output = range[0]+(input-range[1])
            break
    #print("output: " +  str(output))
    return output

def subCalculation(queue,seed,s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l,seedLocations):
    print('I am subcalculation process %d' % (getpid()))
    print("seed: " +  str(seed))
    soil = findCorrespondingRange(seed, s_to_s)
    #print("seed to soil: " +  str(soil), end="\n\n")
    fertilizer = findCorrespondingRange(soil, s_to_f)
    #print("soil to fertilizer: " +  str(fertilizer), end="\n\n")
    water = findCorrespondingRange(fertilizer, f_to_w)
    #print("fertilizer to water: " +  str(water), end="\n\n")
    light = findCorrespondingRange(water, w_to_l)
    #print("water to light: " +  str(light), end="\n\n")
    temperature = findCorrespondingRange(light, l_to_t)
    #print("light to temperature: " +  str(temperature), end="\n\n")
    humidity = findCorrespondingRange(temperature, t_to_h)
    #print("temperature to humidity: " +  str(humidity), end="\n\n")
    location = findCorrespondingRange(humidity, h_to_l)
    #print("humidity to location: " +  str(location), end="\n\n")
    #print("")
    end_location_time = datetime.datetime.now()
    print("End location calc:", end_location_time, end="\n\n\n\n")
    queue.put(location)

def mainCalculation(queue,seedRange,s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l,locations):
    print('I am maincalculation process %d' % (getpid()))
    print("Starting main calculation")  
    print("Seed Range: " + str(seedRange))
    start_time = datetime.datetime.now()
    print("Start time:", start_time)
    seeds = getSeeds(int(seedRange[0]),int(seedRange[1]))
    seedLocations = []
    q2 = Queue()
    processes2= []
    rets2   = []
    for seed in seeds:
        p2 = Process(target=subCalculation, args=(q2,seed,s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l,seedLocations))
        processes2.append(p2)
        p2.start()
    for p2 in processes2:
        ret2 = q2.get()
        rets2.append(ret2)
    for p2 in processes2:
        p2.join()
    end_time = datetime.datetime.now()
    print("End time:", end_time, end="\n\n\n\n")
    queue.put(min(seedLocations))

def main():
    with open("2023_05.input", "r") as f:
        start_time = datetime.datetime.now()
        print("Start time:", start_time)
        lines = f.read()
        seedRanges = getSeedsRanges(lines)
        locations = []
        (s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l) = getRangeBlocks(lines)
        #print("Seed to Soil: " + str(s_to_s))
        #print("Soil to Fertilizer: " + str(s_to_f))
        #print("Fertilizer to Water: " + str(f_to_w))
        #print("Water to Light: " + str(w_to_l))
        #print("Light to Temperature: " + str(l_to_t))
        #print("Temperature to Humidity: " + str(t_to_h))
        #print("Humidity to Location: " + str(h_to_l))
        q = Queue()
        processes = []
        rets    = []
        for seedRange in seedRanges:
            p = Process(target=mainCalculation, args=(q,seedRange,s_to_s,s_to_f,f_to_w,w_to_l,l_to_t,t_to_h,h_to_l,locations))
            processes.append(p)
            p.start()
        for p in processes:
            ret = q.get()
            rets.append(ret)
        for p in processes:
            p.join()
        print("All processes joined")
        locations.append(min(rets))
        print("Locations calculated")
        print(min(locations))


if __name__ == "__main__":
    main()