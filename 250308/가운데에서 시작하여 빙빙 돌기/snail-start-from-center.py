N = int(input())
grid = [[0] * N for _ in range(N)]

x, y = N // 2, N // 2 # initial position
start_num = 1 # first number
grid[x][y] = start_num # alocate 1 at the center

# direction (right -> top -> left -> bottom)
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N and grid[x][y] == 0

# Spiral movement: Expanding outward
step_size = 1  # Step size increases every two turns
while start_num < N * N:
    for i in range(4): # Iterate over directions (Right → Up → Left → Down)
        for _ in range(step_size):
            if start_num >= N * N:  # If grid is full, stop
                break
            x += dx[i]
            y += dy[i]
            if in_range(x, y):
                start_num += 1
                grid[x][y] = start_num
        if i % 2 == 1:  # Increase step size every two directions
            step_size += 1

# print result
for row in grid:
    print(' '.join(map(str, row)))
    