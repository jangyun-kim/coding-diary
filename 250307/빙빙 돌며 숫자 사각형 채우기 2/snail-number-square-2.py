def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

N, M = map(int, input().split())

arr = [[0 for i in range(M)] for i in range(N)]

x, y = 0, 0
dir_num = 0 # indicate donw side

for i in range(1, N * M + 1):
    arr[x][y] = i

    nx = x + dx[dir_num]
    ny = y + dy[dir_num]

    if not in_range(nx, ny) or arr[nx][ny] is not 0:
        dir_num = (dir_num - 1) % 4

    x = x + dx[dir_num]
    y = y + dy[dir_num]

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=' ')
    print()
