
def count_change(money, coins):
    coins.sort()
    #print("coins = ", coins)
    #print("money = ", money)
    if coins == []:
        if money == 0:
            return 1
        return 0
    if coins[0] > money:
        return 0
    parts = [[0 for i in range(money+1)] for c in range(len(coins)+1)] #parts[k][n] = number of partitions of n using coins[:k-1]
    for i in range(len(coins)+1):
        parts[i][0] = 1
        parts[i][coins[0]] = 1
    parts[0][coins[0]] = 0
    for amount in range(coins[0]+1, money + 1):
        #for each amount of money, we will compute all the ways to amass it by knowing how many ways we can amass smaller amounts
        for coin_index in range(1, len(coins)+1):
            #we want to compute parts[coins_index][amount] as the sum over all k of
            #parts[coins_index - 1][amount - coins[coins_index - 1]*k]
            #call remains = amount - coins[coins_index - 1], iterate until remains < 0
            remains = amount
            while remains >= 0:
                #print("amount = ", amount)
                #print("coin_index = ", coin_index)
                #print("Parts added = ", parts[coin_index - 1][remains])
                parts[coin_index][amount] += parts[coin_index - 1][remains]
                remains -= coins[coin_index-1]
    #for j in range(money+1):
    #    for i in range(len(coins)+1):
    #        print("parts[", i, "][", j, "] = ", parts[i][j])
    return parts[len(coins)][money]
