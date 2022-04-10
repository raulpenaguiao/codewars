def determinant(matrix):
    l = len(matrix)
    if(l == 0 or l == 1):
        if(l == 0):
            return 1
        return matrix[0][0];
    det = 0
    sign = -1
    for i in range(l):
        sign *= -1
        new_matrix = [[matrix[j][k] for k in range(l) if k != i ] for j in range(1, l)]
        det += sign * matrix[0][i] * determinant(new_matrix)

    return det;
