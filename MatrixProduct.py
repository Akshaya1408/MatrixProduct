def MatrixProduct(matrix, rows, scalar):
    columns = len(matrix[0])

    for i in range(rows):
        for j in range(columns):
            matrix[i][j] *= scalar

    return matrix


if __name__ == "__main__":
    rows = int(input("No of rows : "))

    matrix = []
    for i in range(rows):
        matrix.append(list(map(int, input().split())))

    B = int(input())

    print(MatrixProduct(matrix, rows, B))