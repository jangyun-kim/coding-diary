N = int(input())

# dictionary to record visited position
visited = {}

# Initial position
current_position = 0
visited[current_position] = 0

# list to record the pathway
path = [current_position]

# follow visited position
for _ in range(N):
    x, direction = input().split()
    x = int(x)

    # Move to 'Left'
    if direction == 'L':
        for i in range(x):
            current_position -= 1
            if current_position in visited:
                visited[current_position] += 1
            else:
                visited[current_position] = 1

    # Move to 'Right'
    elif direction == 'R':
        for i in range(x):
            current_position += 1
            if current_position in visited:
                visited[current_position] += 1
            else:
                visited[current_position] = 1

overlap_count = 0
for count in visited.values():
    if count >= 2:
        overlap_count += 1

print(overlap_count)