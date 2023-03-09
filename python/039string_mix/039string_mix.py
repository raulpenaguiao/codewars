def occs(s):
    dic = {}
    for c in s:
        if c in dic:
            dic[c] += 1
        else:
            if c.islower():
                dic[c] = 1
    return dic


def string_from(t, c, w):
    if t <= 1:
        return ""
    ans = w + ":"
    for _ in range(t):
        ans += c
    return ans


def val(l):
    return [-l[0], l[2] + l[1]]


def mix(s1, s2):
    d1 = occs(s1)
    d2 = occs(s2)
    list_of_entries = []
    for c in d1:
        if c in d2:
            if d1[c] > d2[c]:
                list_of_entries.append([d1[c], c, "1"])
            elif d1[c] < d2[c]:
                list_of_entries.append([d2[c], c, "2"])
            else:
                list_of_entries.append([d1[c], c, "="])
        else:
            list_of_entries.append([d1[c], c, "1"])
    for c in d2:
        if not c in d1:
            list_of_entries.append([d2[c], c, "2"])
    list_of_entries.sort(key=val)
    print(list_of_entries)
    return "/".join([string_from(ls[0], ls[1], ls[2]) for ls in list_of_entries if ls[0] > 1])
    # your code
