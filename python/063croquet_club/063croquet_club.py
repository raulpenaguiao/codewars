def f(p):
    if p[0] >= 55 and p[1] > 7:
        return "Senior"
    return "Open"


def open_or_senior(data):
    return [f(p) for p in data]
