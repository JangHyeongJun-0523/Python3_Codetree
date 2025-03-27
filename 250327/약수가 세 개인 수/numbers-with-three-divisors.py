start, end = map(int, input().split())
cnt = int(0)
devider = int(0)

for i in range(start, end+1):
    for j in range(i):
        if i % (j+1) == 0:
            devider += 1

    if devider == 3:
        cnt += 1
    devider = 0

print(cnt)