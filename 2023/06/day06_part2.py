import math as Math

with open("2023_06.input", "r") as f:
  lines = f.readlines()
  #Parse Time and distance, by:
  #taking the first line (lines[0])
  #stripping it of \n characters (strip())
  #Splitting it on : and only taking the second half (split(":")[1])
  #Splitting it on spaces and joining it back together (split() and join())
  time = int(''.join(lines[0].strip().split(":")[1].split()))
  distance = int(''.join(lines[1].strip().split(":")[1].split()))
  print("Time: ", time)
  print("Distance: ", distance)
  numberOfWins = 0
  previousDistance = 0
  #calculate the range of speeds that can be used. If we go over half the time of the race, we can't win.	so we're ignoring those speeds.
  #In theory, we coul just see when the first time that wins occurs, and use that as a calculation to count the total times that can win.
  #instead, we generate a range, and then using list(map(lamda , we calculate the speed for each item in the ranges array.))
  #we then filter out any speeds that don't win.
  #if the time is even, we can't win on the last second, so we subtract 1 from the total number of wins.
  ranges = range(1, Math.floor(time/2)+1)
  r = list(map(lambda speed: speed * (time - speed), ranges))
  r = list(filter(lambda distanceTravelled: distanceTravelled > distance, r))
  if time % 2 == 0:
    numberOfWins = len(r) * 2 - 1 
  else:
    numberOfWins = len(r) * 2;
  
  print(numberOfWins)
