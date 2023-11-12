import math
import time

# Closest Pair of Points (Divide and Conquer) 

def distance(fp, sp):
    #calculate distance between TWO points
    x, y = fp
    a, b = sp
    return math.sqrt((abs(x - a)) ** 2 + (abs(y - b)) ** 2)


def cp_brute(points):
    #check distance between each point (when more than 2)
    smalest_dist_points = []
    smalest_distance = 999999

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < smalest_distance:
                smalest_distance = dist
                smalest_dist_points = [points[i], points[j]]
    return smalest_dist_points, smalest_distance


def closest_pair2(points):
    pair = []

    n = len(points)

    # last step in recurssion, return distance and two clossest point from the smallest window
    if n == 2:
        return (points[0], points[1]), distance(points[0], points[1])
    if n == 3:
        return cp_brute(points)

    # divide points
    mid = n // 2
    midpoint = points[mid]
    pair_l, dl = closest_pair2(points[:mid])
    pair_r, dr = closest_pair2(points[mid:])
    # check if closest points are in the left or right window
    d = min(dl, dr)
    if d == dl:
        pair = pair_l
    else:
        pair = pair_r

    # get points that X coordinates are in range +/- d from boundary between left and rigth window
    S = []
    for point in points:
        if (midpoint[0] + d >= point[0] >= midpoint[0] - d):
            S.append(point)

    # sort by Y coordinate
    S_sorted = sorted(S, key=lambda point: point[1])

    # check each point in S_sorted
    # no need to check distance between all point, only for next seven, because
    # other point can't have distance less than alredy smallest d
    for i in range(len(S_sorted)):
        for j in range(1, min(8, len(S_sorted)-i)):
            dist_check = distance(S_sorted[i], S_sorted[i + j])
            d = min(d, dist_check)
            if d == dist_check:
                pair = (S_sorted[i], S_sorted[i + j])
    return pair, d


# main function
def closest_pair(points):
    start_time = time.time()
    # sort by X coordinate
    points_sorted = sorted(points, key=lambda point: point[0])
    result = closest_pair2(points_sorted)[0]
    print(time.time() - start_time)
    return result
