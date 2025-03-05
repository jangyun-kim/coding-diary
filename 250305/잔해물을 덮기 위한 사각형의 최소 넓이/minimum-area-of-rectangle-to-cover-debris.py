def area(x1, y1, x2, y2):
    ##주어진 좌표를 이용하여 직사각형의 넓이를 계산
    return max(0, (x2 - x1) * (y2 - y1))

def intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ##두 직사각형이 겹치는 영역의 넓이를 계산
    ix1 = max(ax1, bx1)
    iy1 = max(ay1, by1)
    ix2 = min(ax2, bx2)
    iy2 = min(ay2, by2)

    # If there is no actual intersection, return 0
    if ix1 >= ix2 or iy1 >= iy2:
        return 0, 0, 0, 0  # No valid intersection

    return ix1, iy1, ix2, iy2

def min_covering_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    """Finds the minimum rectangle that covers the remaining part of A after B is placed."""

    # Get the intersection coordinates
    ix1, iy1, ix2, iy2 = intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

    # If B completely covers A, return 0
    if (ix1, iy1, ix2, iy2) == (ax1, ay1, ax2, ay2):
        return 0

    # Remaining parts of A
    uncovered_regions = []

    # Left part of A (if exists)
    if ax1 < ix1:
        uncovered_regions.append((ax1, ay1, ix1, ay2))

    # Right part of A (if exists)
    if ax2 > ix2:
        uncovered_regions.append((ix2, ay1, ax2, ay2))

    # Bottom part of A (if exists)
    if ay1 < iy1:
        uncovered_regions.append((ax1, ay1, ax2, iy1))

    # Top part of A (if exists)
    if ay2 > iy2:
        uncovered_regions.append((ax1, iy2, ax2, ay2))

    # If only one region remains, return its area
    if len(uncovered_regions) == 1:
        x1, y1, x2, y2 = uncovered_regions[0]
        return area(x1, y1, x2, y2)

    # If multiple regions remain, find the minimum bounding rectangle
    min_x = min(rect[0] for rect in uncovered_regions)
    min_y = min(rect[1] for rect in uncovered_regions)
    max_x = max(rect[2] for rect in uncovered_regions)
    max_y = max(rect[3] for rect in uncovered_regions)

    return area(min_x, min_y, max_x, max_y)

# 입력
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())

# 최소 직사각형의 넓이 계산
result = min_covering_rectangle(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)

# 결과 출력
print(result)
