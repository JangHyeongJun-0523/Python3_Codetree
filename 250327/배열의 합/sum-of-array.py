numbers = [list(map(int, input().split())) for _ in range(4)]

for i in range(4):
    summation = 0
    for j in range(4):
        summation += numbers[i][j]
    print(summation)