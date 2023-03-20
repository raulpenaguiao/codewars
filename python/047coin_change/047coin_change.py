def count_change(money, coins):
    change = [[0 for j in coins] + [0] for i in range(money+1)]
    change[0][0] = 1
    #change[j][i] = number of ways of making change for j$ with coins[:i]
    for index, den in enumerate(coins):
        k = 0
        while k <= money:
            for i in range(k, money + 1):
                change[i][index+1] += change[i-k][index]
            k += den# = coins[index]
    return change[money][len(coins)]
