matrix = [list(map(int, input().split())) for _ in range(4)]
cnt = int(0)

for i in range(4):
    for j in range(4):
        if matrix[i][j] % 5 == 0:
            cnt += 1

print(cnt)