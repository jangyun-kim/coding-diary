x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

def intersection_area(x1, y1, x2, y2, x3, y3, x4, y4):
    ix1 = max(x1, x3)
    iy1 = max(y1, y3)
    ix2 = min(x2, x4)
    iy2 = min(y2, y4)

    if ix1 >= ix2 or iy1 >= iy2:
        return 0

    return (ix2 - ix1) * (iy2 - iy1)

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

area_A = (x2[0] - x1[0]) * (y2[0] - y1[0])
area_B = (x2[1] - x1[1]) * (y2[1]- y1[1])

intersection_A = intersection_area(x1[0], y1[0], x2[0], y2[0], x1[2], y1[2], x2[2], y2[2])
intersection_B = intersection_area(x1[1], y1[1], x2[1], y2[1], x1[2], y1[2], x2[2], y2[2])

remaining_area_A = area_A - intersection_A
remaining_area_B = area_B - intersection_B

result = remaining_area_A + remaining_area_B

print(result)

