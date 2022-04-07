import math


def is_really_interesting(number, awesome):
    if number in awesome:
        return True
    n = number
    digs = []
    n_digs = 0
    while(n > 0):
        digs += [n%10]
        n /= 10
        n = math.floor(n)
        n_digs+=1
    if n_digs < 3:
        return False
    #check if it is of the form n00000
    bool = True
    for i in range(n_digs - 1):
        if digs[i] != 0:
            bool = False
    if bool:
        return True
    #check if the number is of the form nnnnnnn
    dig = digs[0]
    bool = True
    for i in range(n_digs - 1):
        if dig != digs[i+1]:
            bool = False
    if bool:
        return True
    #check if digits are sequentially increasing
    
    bool = True
    for i in range(n_digs - 1):
        x = digs[i] - digs[i + 1]
        if x !=  1 and x != -9:
            bool = False
    if bool:
        return True
    
    #check if digits are sequentially decreasing
    
    bool = True
    for i in range(n_digs-1):
        x = digs[i] - digs[i + 1]
        if x !=  -1:
            bool = False
    if bool:
        return True
    #check if palindrome
    
    bool = True
    for i in range(n_digs):
        if digs[i] != digs[n_digs - 1 - i]:
            bool = False
    if bool:
        return True
    
    
    
    
    return False
    

def is_interesting(number, awesome_phrases):
    if(is_really_interesting(number, awesome_phrases)):
        return 2
    if(is_really_interesting(number + 1, awesome_phrases) or is_really_interesting(number + 2, awesome_phrases)):
        return 1
    return 0
