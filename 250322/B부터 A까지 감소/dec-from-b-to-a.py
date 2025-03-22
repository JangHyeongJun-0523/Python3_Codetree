inp=input()
arr=inp.split()
a=int(arr[0])
b=int(arr[1])

for _ in range(b, a-1, -1):
    print(b, end=" ")
    b-=1