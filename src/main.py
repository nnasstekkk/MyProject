n = int(input("Введите количество строк(n): "))
m = int(input("Введите количество столбцов(m): "))

matrix = []
print("Введите элементы матрицы построчно:")

for i in range(n):
    row = []
    for j in range(m):
        value = float(input(f"Введите элемент [{i+1}][{j+1}]: "))
        row.append(value)
    matrix.append(row)

print("Вывод матрицы по столбцам:")
for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=" ")
    print()