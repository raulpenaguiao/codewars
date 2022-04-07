import math

def d(n):
    number = n
    digs = []
    while(number > 0):
        digs += [number % 10]
        number //= 10
    digs.reverse()
    return digs

def to_number(l):
    ans = ''.join([str(x) for x in l])
    return int(ans)

def next_smaller(n):
    digs = d(n)
    n_digs = len(digs)
    index = n_digs - 2
    while(index >= 0 and digs[index] <= digs[index+1]):
        index-= 1
    if index < 0:
        return -1
    #now we find largest element that is smaller than digs[i] 
    max_index = index+1
    max = digs[index+1]
    for i in range(index+2, n_digs):
        if max < digs[i] and digs[i] < digs[index]:
            max = digs[i]
            max_index = i
    trail = []
    for i in range(index, n_digs):
        if i != max_index:
            trail += [digs[i]]
    trail.sort(reverse =  True)
    ans = [digs[t] for t in range(index)] +  [max] +trail
    if ans[0] == 0:
        return -1
    return to_number(ans)
