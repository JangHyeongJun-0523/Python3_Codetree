arr=list(input().split(" "))

if len(arr[0]) > len(arr[1]):
    print(arr[0], end=" ")
    print(len(arr[0]))
elif len(arr[0]) < len(arr[1]):
    print(arr[1], end=" ")
    print(len(arr[1]))
else:
    print("same")