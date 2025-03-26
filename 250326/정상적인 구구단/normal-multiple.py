number = int(input())

for i in range(1, number+1):
    for ii in range(1, number+1):
        print(f"{i} * {ii} = {i * ii}", end="")
        if ii < number:
            print(end=", ")
        else:
            print()