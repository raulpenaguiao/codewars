def spiralize(size):
    if size <= 4:
        if size == 1:
            return [[1]]
        if size == 2:
            return [[1, 1], [0, 1]]
        if size == 3:
            return [[1, 1, 1], [0, 0, 1], [1, 1, 1]]
        return [[1, 1, 1, 1], [0, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 1]]
    mat = spiralize(size-4)
    mat = [[1 for _ in range(size)], [0 for _ in range(size)]] + mat + [[0 for _ in range(size)], [1 for _ in range(size)]]
    mat[1][size-1] = 1
    mat[size-2][0] = 1
    mat[size-2][size-1] = 1
    for i in range(2, size-2):
        mat[i] = [1, 0] + mat[i] + [0, 1]
    mat[1][0]=0
    mat[2][1]=1
    return mat
