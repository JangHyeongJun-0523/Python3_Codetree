a, b = map(int, input().split())
number = a

while number <= b:
    if number % 2 == 1:
        print(number, end=" ")
        number *= 2
    else:
        print(number, end=" ")
        number += 3