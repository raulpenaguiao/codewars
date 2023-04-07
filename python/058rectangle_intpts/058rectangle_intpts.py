import math

def rectangle_rotation(a, b):
    lx = a/(2*math.sqrt(2))
    ly = b/(2*math.sqrt(2))
    ix = math.floor(lx)
    iy = math.floor(ly)
    rx = lx - ix
    ry = ly - iy
    ans = (ix*2 + 1)*(iy*2 + 1)
    #print("a = ", a, " - b = ", b, " - lx = ", lx, " - ly = ", ly, " - ix = ", ix, " - iy = ", iy, " - rx = ", rx, " - ry = ", ry)
    #print("ans = ", ans)
    if rx >= 0.5:
        if ry >= 0.5:
            ans += (ix+1)*(iy+1)*4 
        else:
            ans += iy*(ix+1)*4
    else:
        if ry >= 0.5:
            ans += (iy+1)*ix*4
        else:
            ans += ix*iy*4
    #print(ans)
    return ans
