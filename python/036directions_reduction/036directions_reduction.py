def match(c1, c2):
    if c1 == "NORTH" and c2 == "SOUTH":
        return True
    if c1 == "SOUTH" and c2 == "NORTH":
        return True
    if c1 == "EAST" and c2 == "WEST":
        return True
    if c1 == "WEST" and c2 == "EAST":
        return True
    return False

def dirReduc(arr):
    l = len(arr)
    i = 1
    while i < l:
        if match(arr[i], arr[i-1]):
            return dirReduc(arr[0:i-1] + arr[i+1:l])
        i+=1
    return arr
