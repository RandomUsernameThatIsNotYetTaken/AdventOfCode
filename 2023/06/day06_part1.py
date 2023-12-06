import numpy

with open("2023_06.input", "r") as f:
  lines = f.readlines()
  times = [int(x) for x in lines[0].strip().split(":")[1].split()]
  distances = [int(x) for x in lines[1].strip().split(":")[1].split()]
  print("Times: ", times)
  print("Distances: ", distances)
  wins = []
  for i in range(len(times)):
    numberOfWins=0
    for durationPush in range(times[i]):
      raceDuration = times[i]
      print("Race Duration: ", times[i])
      speed = durationPush
      timeRemaining = raceDuration - durationPush
      print("Speed: ", speed)
      distanceTravelled = speed * timeRemaining
      print("Distance: ", distanceTravelled)
      if distanceTravelled >= distances[i]:
        numberOfWins += 1
    wins.append(numberOfWins)
  print(wins)
  print(numpy.prod(wins))