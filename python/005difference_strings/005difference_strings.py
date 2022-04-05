def count(char, str):
    count = 0
    for c in str:
        if c == char:
            count+= 1
    return count
def parser(list):
    str = list[2] + ":"
    for i in range(list[1]):
        str += list[0]
    return str
def keyLen(st):
    return[-len(st), st]
def mix(s1, s2):
    occs = {}
    for char in s1:
        occs[char] = 0
    for char in s2:
        occs[char] = 0
    diffDict = []
    for char in occs:
        if(char.islower()):#check if it is lowercase letter or digit
            a = count(char, s1)
            b = count(char, s2)
            if a == b and b > 1:
                diffDict +=[[char, a, "="]]
            elif a < b and b > 1:
                diffDict +=[[char, b, "2"]]
            elif  a > 1:
                diffDict +=[[char, a, "1"]]
    arr = list(map(parser, diffDict))
    arr.sort(key = keyLen)
    return "/".join(arr)
# your code
    
