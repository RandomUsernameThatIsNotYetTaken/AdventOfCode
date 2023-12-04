def getCardandHand(line):
  cards = []
  hands = []
  for i in range(0, len(line)):
    line = line.strip()
    if line[i] == ":":
      y = i
    if line[i] == "|":
      cards = line[y+1:i].strip().split()
      hands = line[i+1:].strip().split()
      break
  return (cards,hands)

def calculateScore(card, hand):
  score = 0
  firstMatch = False
  for cardNumber in card:
    for handNumber in hand:
      if cardNumber == handNumber:
        if firstMatch:
          score = score*2
        else:
          score = score + 1
        firstMatch = True
  return score

with open("2023_04.input", "r") as f:
  score=0
  lines = f.readlines()
  for line in lines:
    (card,hand) = getCardandHand(line)
    scoreCard = calculateScore(card,hand)
    score = score + scoreCard
print(score)
    
    