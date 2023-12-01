

def getDigits(line):)
  digits = []
  for c in line:
    if c.isdigit():
      digits.append(int(c))
  return [digits[0],digits[-1]]


with open("2023_01.input", "r") as f:
  digits =[getDigits(line) for line in f.readlines()]
  sumOfConcattedDigits = sum(int(str(digit[0]) + str(digit[1])) for digit in digits)
  print(sumOfConcattedDigits)
      
    