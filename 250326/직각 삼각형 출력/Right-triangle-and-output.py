number = int(input())

for i in range(1, number+1):
    print("*", end="")
    for ii in range(i-1):
        print("**", end="")
    print()
