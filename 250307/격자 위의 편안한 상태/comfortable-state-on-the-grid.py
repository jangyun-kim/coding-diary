# enter input
N, M = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(M)]

# N x N
grid = [[0] * N for _ in range(N)]

# set direction(up, down, left, right)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# To Do
for r, c in points:  # input point (1-based index)
    r -= 1
    c -= 1
    grid[r][c] = 1  # coloring

    # check comfort level 
    count = 0
    for i in range(4):
        nr, nc = r + dx[i], c + dy[i]  # around points
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 1:
            count += 1

    # comfort level = 1, uncomfort level = 0.
    print(1 if count == 3 else 0)