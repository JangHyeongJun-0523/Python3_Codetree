n = int(input())
arr = []
input_number = 0

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    arr.append(row)

for j in range(n):
    if j % 2 == 0:
        input_number += 1
        for i in range(n):
            arr[i][j] = input_number
            input_number += 1
    else:
        input_number -= 1
        for i in range(n):
            arr[i][j] = input_number
            input_number -= 1

for i in range(n):
    for j in range(n):
        print(arr[i][j], end="")
    print()
