N = int(input())

x, y = 0, 0
dir_num = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for _ in range(N):
    dir_c, dist = map(str, input().split())
    dist = int(dist)

    for i in range(dist):
        if dir_c == 'N':
            dir_num = 3
        elif dir_c == 'E':
            dir_num = 0
        elif dir_c == 'S':
            dir_num = 1
        elif dir_c == 'W':
            dir_num = 2

        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)