numbers=int(input())
arr=list(map(float, input().split(" ")))
arr=list(map(int, arr))

for i in range(numbers-1, -1, -1):
    if arr[i] % 2 == 0:
        print (arr[i], end=" ")

    elif arr[i] == 0:
        print (arr[i], end=" ")