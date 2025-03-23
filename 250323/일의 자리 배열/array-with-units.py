arr=list(map(int, input().split()))
i=int(0)

while len(arr) < 10:
    new_num = arr[i] + arr[i+1]
    if new_num < 10:
        arr.append(new_num)
    else:
        new_num = new_num - 10
        arr.append(new_num)
    i += 1

for x in range(len(arr)):
    print(arr[x], end=" ")
