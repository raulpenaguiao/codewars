def longest_slide_down(pyramid):
    n = len(pyramid)
    max_pyramid = [[0 for j in range(i+1)] for i in range(n)]
    print(max_pyramid)
    for i in range(n):
        for j in range(i+1):
            max_pyramid[i][j] = pyramid[i][j]
            if j < i:
                max_pyramid[i][j] = max_pyramid[i-1][j] + pyramid[i][j] # for the moment this only assumes that we have non-negative numbers
            if j > 0:
                max_pyramid[i][j] = max(max_pyramid[i][j], max_pyramid[i-1][j-1] +  pyramid[i][j] )
    max_value = max_pyramid[n-1][0]
    for i in range(n-1):
        if max_value < max_pyramid[n-1][i+1]:
            max_value = max_pyramid[n-1][i+1]
    return max_value
        
    # TODO: write some code...
    pass
