import sys

input = sys.stdin.readline
Point = tuple[int]

def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1, p2, p3, p4 = (x1, y1), (x2, y2), (x3, y3), (x4, y4)

ccw1, ccw2, ccw3, ccw4 = ccw(p1, p2, p3), ccw(p1, p2, p4), ccw(p3, p4, p1), ccw(p3, p4, p2)
if ccw1 * ccw2 <= 0 and ccw3 * ccw4 <= 0:
    if ccw1 * ccw2 == 0 and ccw3 * ccw4 == 0:
        if (max(p1[0], p2[0]) >= min(p3[0], p4[0]) and max(p3[0], p4[0]) >= min(p1[0], p2[0]))\
            and (max(p1[1], p2[1]) >= min(p3[1], p4[1]) and max(p3[1], p4[1]) >= min(p1[1], p2[1])):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)