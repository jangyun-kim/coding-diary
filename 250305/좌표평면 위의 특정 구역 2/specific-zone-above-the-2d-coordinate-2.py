import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# 각각의 점을 뺀 모든 경우를 고려
# i번 점을 뻈다고 가정했을 때
ans = sys.maxsize
for i in range(n):
    # i번 점을 제외한 모든 점들에 대해
    # 커버하는 최소 직사각형 넓이 구하기
    # => 최소 x, 최대 x, 최소 y, 최대 y를 구한다.
    minx, miny = sys.maxsize, sys.maxsize
    maxx, maxy = -sys.maxsize, -sys.maxsize
    for j in range(n):
        if i == j:
            continue
        minx = min(minx, x[j])
        maxx = max(maxx, x[j])
        miny = min(miny, y[j])
        maxy = max(maxy, y[j])

    area = (maxx - minx) * (maxy - miny)
    ans = min(ans, area)

print(ans)