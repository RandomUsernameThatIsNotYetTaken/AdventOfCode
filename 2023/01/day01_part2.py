def replaceRegex(line):
  numbers_dictionary = {'one':'o1ne','two':'t2wo','three':'th3ree','four':'fo4ur','five':'fi5ve','six':'s6ix','seven':'seve7n','eight':'ei8ght','nine':'n9ine','zero':'z0ero'}
  for key in numbers_dictionary:
    if(key in line):
      line = line.replace(key,numbers_dictionary[key])
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
      
    