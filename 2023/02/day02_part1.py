
def parseLine(line):
  line = line.split(":")
  game = line[0].replace("Game ", "");
  hands = line[1].split(";")
  hands_parsed = []
  for hand in hands:
    hand_parsed = [0,0,0]
    hand = hand.strip().split(", ")
    for card in hand:
      card = card.split(" ")
      if card[1] == "red":
        hand_parsed[0] = card[0]
      elif card[1] == "green":
        hand_parsed[1] = card[0]
      elif card[1] == "blue":
        hand_parsed[2] = card[0]
    hands_parsed.append(hand_parsed)
  return (game, hands_parsed)

def possibleHands(hands):
  for hand in hands:
    if int(hand[0]) > 12 or int(hand[1]) > 13 or int(hand[2]) > 14:
      return False
  return True

totalGames = 0
with open("2023_02.input", "r") as f:
  lines = f.readlines()
  for line in lines:
    game, hands = parseLine(line)
    possible = possibleHands(hands)
    if possible:
      totalGames += int(game)
print(totalGames)