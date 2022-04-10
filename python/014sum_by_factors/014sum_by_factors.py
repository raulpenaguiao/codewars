from math import sqrt

def sum_for_list(lst):
    if lst == []:
        return 1
    max = abs(lst[0])
    for i in range(len(lst)-1):
        if abs(lst[i+1]) > max:
            max = abs(lst[i+1])
    
    primes_list = [2, 3, 5, 7, 11, 13]
    vis_primes = [(i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0 and i%11 != 0 and i%13 != 0) for i in range(max+1)]
    k = 17
    while(k * k <= max):
        if(vis_primes[k]):
            primes_list += [k]
            l = k*k
            while(l <= max):
                vis_primes[l] = False
                l+=2*k
        k+= 2
    while(k <= max):
        if(vis_primes[k]):
            primes_list+= [k]
        k+= 2
    count = [ [prime, 0, False] for prime in primes_list]
    
    for i in range(len( primes_list)):
        for x in lst:
            if x % primes_list[i] == 0:
                count[i][1] += x
                count[i][2] = True
    
    #print("primes = ", primes_list)
    
    
    
    return [[ls[0], ls[1]] for ls in count if ls[2]]#small problem if sum is zero
