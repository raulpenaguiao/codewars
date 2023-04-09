def array_diff(a, b):
    ans = []
    for item in a:
        if not(item in b):
            ans += [item]
    return ans
