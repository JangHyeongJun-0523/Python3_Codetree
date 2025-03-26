Three = int(0)
Five = int(0)

for _ in range(10):
    number = int(input())
    if number % 3 == 0:
        Three += 1
    if number % 5 == 0:
        Five += 1

print(f"{Three} {Five}")