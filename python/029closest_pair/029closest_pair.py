def dist(point0, point1):
    return (point0[0] - point1[0])** 2 + (point0[1] - point1[1])** 2


def y_coord(pt):
    return pt[1]

def closest_pair(points):
    if len(points) == 2:
        return points
    if len(points) == 3:
        l1 = dist(points[0], points[1])
        l2 = dist(points[0], points[2])
        l3 = dist(points[1], points[2])
        if l1 < l2:
            if l1 < l3:
                return (points[0], points[1])
            else:
                return (points[1], points[2])
        else:
            if l2 < l3:
                return (points[0], points[2])
            else:
                return (points[1], points[2])
    #print("computing in ", points)
    s_points = sorted(points)
    l = len(points)
    lh = l//2
    pl = ()
    pr = ()
    for i in range(lh):
        pl += (s_points[i],)
    #print("pl = ", pl)
    for i in range(lh, l):
        pr += (s_points[i],)
    #print("pr = ", pr)
    pl = closest_pair(pl)
    pr = closest_pair(pr)
    dl = dist(pl[0], pl[1])
    dr = dist(pr[0], pl[1])
    d = min(dl, dr)
    #Now we check for all the points that are at most distance d from the other half
    xrmax = s_points[lh-1][0]
    xlmin = s_points[lh][0]
    l_points = (pt for pt in points if pt[0] < xrmax + d or pt[0] > xlmin - d)
    l_points = sorted(l_points, key = y_coord)
    #print("l_points = ", l_points)
    #print("xlmin = ", xlmin)
    #print("xrmax = " , xrmax)
    if d == dr:
        p = pr
    elif d == dl:
        p = pl
    for i in range(len(l_points)):
        for j in range(i-5, i+5):
            if j>= 0 and j < len(l_points) and i != j:
                if dist(l_points[i], l_points[j]) < d:
                    d = dist(l_points[i], l_points[j])
                    p = (l_points[i], l_points[j])
    print(p)
    return p
