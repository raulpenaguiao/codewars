from fractions import gcd
import math

def lcm_list(list):
    if(len(list) == 0):
        return 1
    l = len(list)
    if(l == 1):
        return list[0]
    x = list[l-1] * list[l-2] / gcd(list[l-1], list[l-2])
    list.pop()
    list[l-2] = x
    return lcm_list(list)
    
def convert_fracts(lst):
    D = lcm_list([l[1] for l in lst])
    return [[l[0]*math.floor(D/l[1]), D] for l in lst]
