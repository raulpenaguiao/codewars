def is_pangram(s):
    chars = "qwerttzuiopasdfgghjklyxcvbbnm"
    for c in chars:
        flag = False
        for t in s:
            if t.lower() == c:
                flag = True
        if flag == False:
            return False
    return True
