number = int(input())
count=int(0)

for i in range(1, number+1, 1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
        continue
    count += 1

print(count)