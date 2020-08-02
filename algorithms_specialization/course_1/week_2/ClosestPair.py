import math


def distanceBetweenPoints(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def closestSplitPair(px, py, delta):
    xBar = px[len(px)//2][0]
    strip = [y for y in py if(xBar - delta) < y[0] < (xBar + delta)]
    closePair = None
    minDistance = delta
    if len(strip) > 1:
        for i in range(len(strip)):
            for j in range(i+1, min(7, len(strip))):
                dist = distanceBetweenPoints(strip[i], strip[j])
                if dist < minDistance:
                    minDistance = dist
                    closePair = [strip[i], strip[j]]
    return closePair, minDistance


def closestPair(px):
    if len(px) < 4:
        min_dist = None
        closePair = []
        for i in range(len(px)):
            for j in range(i+1, len(px)):
                dist = distanceBetweenPoints(px[i], px[j])
                if not min_dist or dist < min_dist:
                    min_dist = dist
                    closePair = [px[i], px[j]]

        y = sorted(px, key=lambda x: x[1])
        return (closePair, min_dist, y)

    qx, rx = px[0:len(px)//2], px[len(px)//2: len(px)]
    py = []
    qPair, d1, qy = closestPair(qx)
    rPair, d2, ry = closestPair(rx)
    i = j = 0
    while (i+j) < len(px):
        if i < len(qy) and (j >= len(ry) or qy[i][1] < ry[j][1]):
            py.append(qy[i])
            i += 1
        else:
            py.append(ry[j])
            j += 1

    delta = min(d1, d2)

    splitPair, d3 = closestSplitPair(px, py, delta)

    minDistace = min(d1, d2, d3)

    if d1 == minDistace:
        return qPair, d1, py
    elif d2 == minDistace:
        return rPair, d2, py
    else:
        return splitPair, d3, py


points = [(1, 2), (2, 5), (10, 21), (6, 12), (4, 13), (11, 23)]
# points = [(1, 2), (6, 1), (4, 3), (8, 9), (7, 5), (3, 7), (2, 6), (5, 8)]

px = sorted(points)

print(closestPair(px))
