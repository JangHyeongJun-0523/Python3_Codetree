number = int(input())

for i in range(1, number+1):
    for _ in range(i):
        print(i, end=" ")
    print()