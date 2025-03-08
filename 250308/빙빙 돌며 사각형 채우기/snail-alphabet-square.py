def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

N, M = map(int, input().split())
arr = [['' for _ in range(M)] for _ in range(N)]

x, y = 0, 0
direction = 0 # indicate right side
current_alph = 'A' # first alphabet

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(N * M):
    arr[x][y] = current_alph  # alocate current alphabet at current position.

    # set next character (after Z, start A)
    current_alph = chr(((ord(current_alph) - ord('A') + 1) % 26) + ord('A'))

    # calculate next position
    nx, ny = x + dx[direction], y + dy[direction]

    if not in_range(nx, ny) or arr[nx][ny] != '':
        direction = (direction + 1) % 4  # right → bottom → left → top cycle
        nx, ny = x + dx[direction], y + dy[direction]

    x, y = nx, ny

for row in arr:
    print(' '.join(row))