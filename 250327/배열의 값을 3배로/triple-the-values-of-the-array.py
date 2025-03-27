arr = [list(map(int, input().split())) for _ in range(3)]
rows = 3
cols = 3
new_matrix = []

for i in range(rows):
    new_row = []
    for j in range(cols):
        new_row.append(arr[i][j] * 3)
    new_matrix.append(new_row)

for i in range(rows):
    for j in range(cols):
        print(new_matrix[i][j], end=" ")
    print()