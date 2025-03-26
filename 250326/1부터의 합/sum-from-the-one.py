number = int(input())
summation = int(0)
lastNumber = int(0)

while summation < number:
    lastNumber += 1
    summation += lastNumber

print(lastNumber)