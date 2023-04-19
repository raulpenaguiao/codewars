def digs(n, base = 10):
    if n < base:
        return [n]
    return digs(n//base) + [n%base]

def narcissistic( value ):
    dl = digs(value)
    d = len(dl)
    return sum([a**d for a in dl]) == value
    return False # Code away
