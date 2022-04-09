def count_change(money, coins):
    if len(coins) <= 1:
        if len(coins) == 1 and money % coins[0] == 0:
            return 1
        if money == 0:
            return 1
        return 0
    count = 0
    coin = coins[0]
    list_coins = coins[1:]
    remaning_money = money
    while(remaning_money >= 0):
        count += count_change(remaning_money, list_coins)
        remaning_money -= coin
    return count
    # your implementation here
