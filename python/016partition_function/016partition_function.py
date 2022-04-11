

def exp_sum(n):
    parts = [[0 for i in range(n+1)] for i in range(n+1)] #parts[n][k] = number of partitions of n into parts of size > k 
    for i in range(n+1):
        parts[0][i] = 1
    parts[1][0] = 1
    for i in range(2, n+1):
        parts[i][i-1] = 1
        for j in range(i-1, 0, -1):
            block = i - j
            parts[i][j-1] = parts[i][j]
            while(block >= 0):
                parts[i][j-1] += parts[block][j]
                block -= j
    return parts[n][0]
