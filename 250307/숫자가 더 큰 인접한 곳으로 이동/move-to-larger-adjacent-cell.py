N, r, c = map(int, input().split())
a = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        a[i][j] = row[j - 1]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


x, y = r, c


print(a[x][y], end=" ")

while True:
    next_x, next_y = -1, -1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 1 <= nx <= N and 1 <= ny <= N and a[nx][ny] > a[x][y]:
            next_x, next_y = nx, ny
            break

    if next_x == -1 and next_y == -1:
        break

    x, y = next_x, next_y
    print(a[x][y], end=" ")