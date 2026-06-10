#MATRIX_2D_List

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
matrix = []
for i in range(rows):
    while True:
        row = [int(x) for x in input(f"Enter row {i+1}: ").split()]
        if len(row) == cols:
            matrix.append(row)
            break
        else:
            print(f"Error! Enter exactly {cols} values.")
print("Matrix:")
for row in matrix:
    print(row)
