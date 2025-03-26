fruits = ["apple", "banana", "grape", "blueberry", "orange"]
text = input()
cnt = int(0)

for fruit in fruits:
    if fruit[2] == text or fruit[3] == text:
        print(fruit)
        cnt += 1

print(cnt)