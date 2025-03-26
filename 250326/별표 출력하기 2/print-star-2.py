number = int(input())

for i in range(number, 0, -1):
    for ii in range(i):
        print("*", end=" ")
    print()