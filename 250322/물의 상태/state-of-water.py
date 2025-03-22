inp=input()
temp=int(inp)

if temp < 0:
    print("ice")
elif temp >= 100:
    print("vapor")
else:
    print("water")