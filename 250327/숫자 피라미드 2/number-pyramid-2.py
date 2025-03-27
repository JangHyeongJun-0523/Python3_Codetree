n = int(input())
number = int(1)

for i in range(1, n+1, 1):
    for ii in range(1, i+1, 1):
        print(f"{number}", end=" ")
        number += 1
    print()
