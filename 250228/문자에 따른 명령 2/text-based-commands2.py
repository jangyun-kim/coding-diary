x, y = 0, 0
dir_num = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

dirt = list(input())

for i in range(len(dirt)):
    if dirt[i] == 'L':
        dir_num = (dir_num + 3) % 4
    elif dirt[i] == 'R':
        dir_num = (dir_num + 1) % 4
    elif dirt[i] == 'F':
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)