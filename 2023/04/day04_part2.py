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

def calculateCopies(card, hand):
  score = 0
  for cardNumber in card:
    for handNumber in hand:
      if cardNumber == handNumber:
          score = score + 1
  return score

def processCardHands(card_hands, copies):
  cardCopies = {}
  score1 = 0
  score2 = 0
  cardCopies = {i: 0 for i in range(1, len(card_hands) + 1)}
  print("cardCopies: ",cardCopies)
  for i in range(1,len(card_hands)+1):
    (card, hand) = card_hands[i-1]
    scoreCard = calculateScore(card, hand)
    score1 = score1 + scoreCard
    copies = calculateCopies(card, hand)
    print("Card: ",i," Copies: ",copies)
    if copies > 0:
      print("range: ", str(range(i+1,i+copies+1)))	
      for y in range(i+1,i+copies+1):
        if cardCopies[y] == 0:
          print("y: ",y," cardCopies: ",cardCopies)
          cardCopies.update({y: 1 + cardCopies[i]})
        else:
          cardCopies.update({y: cardCopies[y] + cardCopies[i] + 1 })
  for key in cardCopies.keys():
    score2 = score2 + cardCopies[key] +1
  print("Returning  score1: ",score1," score2: ",score2)
  return (score1,score2)
        

with open("2023_04.input", "r") as f:
  score=0
  lines = f.readlines()
  card_hands = []
  for line in lines:
    (card,hand) = getCardandHand(line)
    card_hands.append((card,hand))
  (score1,score2) = processCardHands(card_hands,[])
  
print(score1)
print(score2)
    
    