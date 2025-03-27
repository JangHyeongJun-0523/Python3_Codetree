start, end = map(int, input().split())
cnt = int(0)

for i in range(start, end+1):
    if i != 1:
        if (i ** (1/2)) % 1 == 0:
            if (i ** (1/2)) % 2 == 0 and i ** (1/2) != 2:
                continue          
            cnt += 1
print(cnt)