a = [list(map(int, input().split())) for _ in range(3)]
blank = input()
b = [list(map(int, input().split())) for _ in range(3)]

multiplied = []

for i in range(3):
    for j in range(3):
        print(a[i][j]*b[i][j], end=" ")
    print()

