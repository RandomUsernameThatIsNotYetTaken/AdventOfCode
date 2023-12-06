import math as Math

with open("2023_06.input", "r") as f:
  lines = f.readlines()
  time = int(''.join(lines[0].strip().split(":")[1].split()))
  distance = int(''.join(lines[1].strip().split(":")[1].split()))
  print("Time: ", time)
  print("Distance: ", distance)
  numberOfWins = 0
  previousDistance = 0
  ranges = range(1, Math.floor(time/2)+1)
  r = list(map(lambda speed: speed * (time - speed), ranges))
  r = list(filter(lambda distanceTravelled: distanceTravelled > distance, r))
  if time % 2 == 0:
    numberOfWins = len(r) * 2 - 1 
  else:
    numberOfWins = len(r) * 2;
  
  print(numberOfWins)
