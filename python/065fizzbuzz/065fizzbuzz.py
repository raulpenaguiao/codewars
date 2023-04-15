def tri(n):
    return n*(n+1)//2

def solution(n):
    if n < 0:
        return 0
    return 3*tri((n-1)//3)+5*tri((n-1)//5)-15*tri((n-1)//15)
    pass
  
