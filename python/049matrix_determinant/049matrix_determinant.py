def determinant(matrix):
    l = len(matrix)
    if l == 1:
        return matrix[0][0]
    ans = 0
    sign = 1
    for index, item in enumerate(matrix[0]):
        new_matrix = [matrix[j][:index]+matrix[j][index+1:] for j in range(1,l)]
        det = determinant(new_matrix)
        ans += sign*det*item
        sign *= -1
    return ans
