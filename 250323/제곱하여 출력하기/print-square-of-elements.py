n=int(input())
arr=list(map(int, input().split()))
sqr=[x**2 for x in arr]

for x in range(n):
    print(sqr[x], end=" ")