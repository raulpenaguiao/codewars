import math 

def is_square(n):
    if n < 0:
        return False
    k = math.floor(0.5 + math.sqrt(n))
    return k*k == n
