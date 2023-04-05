def pstr(num):
    if num < 10:
        return "0"+str(num)
    return str(num)

def make_readable(seconds):
    tot = seconds
    s = tot%60
    tot //= 60
    m = tot%60
    h = tot // 60
    return pstr(h)+ ":" +  pstr(m) + ":" + pstr(s)
    # Do something
