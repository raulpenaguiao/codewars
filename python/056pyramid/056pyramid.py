
def longest_slide_down(pyramid):
    l = len(pyramid)
    if l == 0:
        return 0
    cum_sum = [[0 for _ in range(j+1)] for j in range(l)]
    cum_sum[0][0] = pyramid[0][0]
    for j in range(1, l):
        cum_sum[j][j] = cum_sum[j-1][j-1] + pyramid[j][j]
        cum_sum[j][0] = cum_sum[j-1][0] + pyramid[j][0]
        for i in range(1, j):
            cum_sum[j][i] = max(cum_sum[j-1][i], cum_sum[j-1][i-1])  + pyramid[j][i]            
    return max(cum_sum[l-1])
