import sys

N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

x, y = 0, 0 # start point
dir_num = 0 # 0: East, 1: South, 2: West, 3: North

time_flow = 0
mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

# process moves
for i in range(N):
    move_dir = mapper[dir[i]]

    for _ in range(dist[i]):
        x, y = x + dx[move_dir], y + dy[move_dir]
        time_flow += 1
        if x == 0 and y == 0:
            print(time_flow)
            sys.exit()

# N번 이동했는데도 원점에 도달하지 못한 경우
print(-1)