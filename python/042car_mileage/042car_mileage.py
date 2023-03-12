def dig_list(n):
    if n < 10:
        return [n]
    return dig_list(n//10) + [n%10]

def is_1(l_n):#Is n followed by all zeroes
    l = len(l_n)
    for i in range(l-1):
        if not 0 == l_n[i+1]:
            return False
    return True


def is_2(l_n):#Is every digit the same
    l = len(l_n)
    for i in range(l-1):
        if not l_n[i] == l_n[i+1]:
            return False
    return True

def is_3(l_n):#Are digits sequentially incrementing
    l = len(l_n)
    for i in range(l-1):
        if not (l_n[i] == l_n[i+1]-1 or l_n[i] == l_n[i+1]+9):
            return False
    return True
    
def is_4(l_n):#Are digits sequentially decreasing
    l = len(l_n)
    for i in range(l-1):
        if not l_n[i] == l_n[i+1]+1:
            return False
    return True

def is_5(l_n):#Are digits palindromes
    l = len(l_n)
    for i in range(l):
        if not l_n[i] == l_n[l-i-1]:
            return False
    return True

def is_6(n, a):#Match awesome phrases
    return n in a


def is_interesting(number, awesome_phrases):
    l0 = dig_list(number)
    l1 = dig_list(number+1)
    l2 = dig_list(number+2)
    if number > 99 and (is_1(l0) or is_2(l0) or is_3(l0) or is_4(l0) or is_5(l0) or is_6(number, awesome_phrases)):
        return 2
    if number + 1 > 99 and (is_1(l1) or is_2(l1) or is_3(l1) or is_4(l1) or is_5(l1) or is_6(number+1, awesome_phrases)):
        return 1
    if number + 2 > 99 and (is_1(l2) or is_2(l2) or is_3(l2) or is_4(l2) or is_5(l2) or is_6(number+2, awesome_phrases)):
        return 1
    return 0
    
