import sys

commands = input()


def in_range(x,y):
    return 0 <= x < N and 0 <= y < M

x, y = 0, 0 # start point
dir_num = 3 # indicate north
time_flow = 0 # elapsed time

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# command process
for command in commands:
    time_flow += 1  # elaped 1 second by every command

    if command == 'L':  # turn left
        dir_num = (dir_num - 1) % 4
    elif command == 'R':  # turn right
        dir_num = (dir_num + 1) % 4
    elif command == 'F':  # go to current direction
        x += dx[dir_num]
        y += dy[dir_num]

    # end process immediately when go back to (0,0)
    if x == 0 and y == 0:
        print(time_flow)
        sys.exit()

# if it is not (0, 0) at the end of process
print(-1)