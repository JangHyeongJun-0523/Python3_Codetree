N_rows, M_cols = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(N_rows)]
matrix2 = [list(map(int, input().split())) for _ in range(N_rows)]

matrix01 = []

for i in range(N_rows):
    new_row = []
    for j in range(M_cols):
        if matrix1[i][j] == matrix2[i][j]:
            new_row.append(int(0))
        else:
            new_row.append(int(1))
    matrix01.append(new_row)

for i in range(N_rows):
    for j in range(M_cols):
        print(matrix01[i][j], end=" ")
    print()