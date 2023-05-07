def solution(text, ending):
    l1 = len(text)
    l2 = len(ending)
    for i in range(1, l2+1):
        if not(text[l1-i] == ending[l2-i]):
            return False
    return True
    # your code here...
    pass
