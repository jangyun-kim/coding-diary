def area(x1, y1, x2, y2):
    ##주어진 좌표를 이용하여 직사각형의 넓이를 계산
    return max(0, (x2 - x1) * (y2 - y1))

def intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ##두 직사각형이 겹치는 영역의 넓이를 계산
    ix1 = max(ax1, bx1)
    iy1 = max(ay1, by1)
    ix2 = min(ax2, bx2)
    iy2 = min(ay2, by2)
    return area(ix1, iy1, ix2, iy2)

def min_covering_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ##첫 번째 직사각형에서 두 번째 직사각형이 덮지 못한 잔여 영역을 최소 직사각형으로 덮는 크기를 계산
    intersection = intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    remaining_area = area(ax1, ay1, ax2, ay2) - intersection

    if min(ay2, by2) - max(ay2, by2) == (ay2 - ay1):
        return remaining_area
    else:
        return remaining_area + intersection

# 입력
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

# 최소 직사각형의 넓이 계산
result = min_covering_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

# 결과 출력
print(result)
