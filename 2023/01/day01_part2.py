def replaceRegex(line):
  print(line)
  numbers = ['one','two','three','four','five','six','seven','eight','nine','zero']
  numbers_reverso = ['eno','owt','eerht','ruof','evif','xis','neves','thgie','enin','orez']
  numbers_replacement = ['o1ne','t2wo','th3ree','fo4ur','fi5ve','s6ix','seve7n','ei8ght','n9ine','z0ero']
  
  for number in numbers:
    if number in line:
      print(number+str(numbers.index(number)+1))
      line = line.replace(number, numbers_replacement[numbers.index(number)])
  for number_reverso in numbers_reverso:
    line_reversed = line[::-1]
    if number_reverso in line_reversed:
      line_reversed = line_reversed.replace(number_reverso,numbers_replacement[numbers_reverso.index(number_reverso)])
      line = line_reversed[::-1]
  print(line)
  return line

def getDigits(line):
  line = replaceRegex(line)
  digits = []
  for c in line:
    if c.isdigit():
      digits.append(int(c))
  print(digits[0],digits[-1])
  return [digits[0],digits[-1]]


with open("2023_01.input", "r") as f:
  digits =[getDigits(line) for line in f.readlines()]
  sumOfConcattedDigits = sum(int(str(digit[0]) + str(digit[1])) for digit in digits)
  print(sumOfConcattedDigits)
      
    