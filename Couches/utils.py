import math


def deg_to_rad(deg):
    return deg * (math.pi / 180.0)


def dist(p1, p2):
    r = 6371
    dlat = deg_to_rad(p2[0] - p1[0])
    dlon = deg_to_rad(p2[1] - p1[1])
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(deg_to_rad(p1[0])) * math.cos(deg_to_rad(p2[0])) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return r * c