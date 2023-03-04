def is_WS(ch):
    return not(ch.isalpha() or ch =="'")


def valid(w):
    return w.count("'") < len(w)


def top_3_words(text):
    l = len(text)
    i = 0
    j = 0 # This is the last non whitespace character
    b = True
    words = []
    while b:
        while j < l and is_WS(text[j]):
            j += 1
        i = j + 1
        while i < l and not(is_WS(text[i])):
            i += 1
        if j < l:
            w = text[j:i].lower()
            if valid(w):
                words.append(w)
            j = i
        else:
            b = False
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    li = [[d[w], w] for w in d]
    li.sort(reverse = True)
    m = min(3, len(li))
    ans = [li[k][1] for k in range(m)]
    return ans
