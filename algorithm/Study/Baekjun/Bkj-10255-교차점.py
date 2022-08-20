import sys

input = sys.stdin.readline
MIIS = lambda: map(int, input().split())
Point = tuple[int]

def ccw(p1: Point, p2: Point, p3: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


T = int(input())

for _ in range(T):
    xl, yb, xr, yt = MIIS()
    x1, y1, x2, y2 = MIIS()

    # 직사각형 내부에 선분의 점이 전부 포함
    if ((xl < x1 < xr) and (yb < y1 < yt)) and ((xl < x2 < xr) and (yb < y2 < yt)):
        print(0)
        continue

    # 직사각형 내부, 직사각형 경계에 각각 점 위치
    if ((xl < x1 < xr) and (yb < y1 < yt)) and ((xl <= x2 <= xr) and (yb <= y2 <= yt)):
        print(1)
        continue
    if ((xl <= x1 <= xr) and (yb <= y1 <= yt)) and ((xl < x2 < xr) and (yb < y2 < yt)):
        print(1)
        continue

    # 직사각형 내부, 직사각형 외부에 각각 점 위치
    if ((xl < x1 < xr) and (yb < y1 < yt)) or ((xl < x2 < xr) and (yb < y2 < yt)):
        print(1)
        continue

    # 직사각형 경계에 점 2개 위치
    if ((xl <= x1 <= xr) and (yb <= y1 <= yt)) and ((xl <= x2 <= xr) and (yb <= y2 <= yt)):
        # 직선이 평행한 경우
        if (x1 == x2) or (y1 == y2):
            print(4)
        else:
            print(2)
        continue

    # 직사각형 경계에 점 1개 위치
    if ((xl <= x1 <= xr) and (yb <= y1 <= yt)) or ((xl <= x2 <= xr) and (yb <= y2 <= yt)):
        if (x1 == x2) or (y1 == y2):
            pass
        else:
            print(1)
        continue