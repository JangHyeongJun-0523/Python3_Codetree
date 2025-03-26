A, B = map(int, input().split())
evenSum = int(0)

for i in range(A, B+1):
    if i % 2 == 0:
        evenSum += i

print(evenSum)
    