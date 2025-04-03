rows, cols = 7, 7
matrix = [[7 - j for j in range(cols)] for i in range(rows)]

for row in matrix:
    print(" ".join(map(str, row)))
