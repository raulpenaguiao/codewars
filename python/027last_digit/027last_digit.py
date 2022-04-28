def last_dig_2(lst):
    if lst == []:
        return 1
    if len(lst) == 1 or lst[1] != 0 or :
        return lst[0]%2
    return 1

def last_dig_4(lst):
    if lst == []:
        return 1
    if lst[0]%2 == 0:
        return ((lst[0]%4) ** last_dig_2(lst[:1])) % 4
    k = lst[0]%4
    if k == 3:
        k = -1
    k = (k ** last_dig_2(lst[:1])) % 4
    if k == -1:
        return 3
    return 1


def last_digit(lst):
    if lst == []:
        return 1
    if lst[0]%5 == 0:
        return lst[0]%10
    if lst[0]%2 == 0:
        N = lst[0]//2
        res = 2
        while(N%2 == 0):
            N //= 2
            res *= 2
        a = last_digit([N%10] + lst[1:])
        b = last_digit([res%10] + lst[1:])
        return (a*b)%10
    
    # Your Code Here
    pass
