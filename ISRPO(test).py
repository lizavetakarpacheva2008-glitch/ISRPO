n = int(input("Введите размер матрицы: "))
matrix = []
for i in range(n):
    row = list(map(int, input(f"Введите {i+1}-ю строку: ").split()))
    matrix.append(row)
transposed = []
for i in range(n):
    new_row = []
    for j in range(n):
        new_row.append(matrix[j][i])
    transposed.append(new_row)
print("Транспонированная матрица:")
for row in transposed:
    print(row)
