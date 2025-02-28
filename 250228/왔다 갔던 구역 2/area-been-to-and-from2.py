N = int(input())

# Initial position
current_position = 0

visited = [0] * 200001

# Calculate an overlaped range
overlap_count = 0

# Movement process by a command
for _ in range(N):
    x, direction = input().split()
    x = int(x)

    # Move to 'Left'
    if direction == 'L':
        for i in range(x):
            current_position -= 1
            if visited[current_position + 100000] == 1:
                overlap_count += 1
            visited[current_position + 100000] += 1

    # Move to 'Right'
    elif direction == 'R':
        for i in range(x):
            current_position += 1
            if visited[current_position + 100000] == 1:
                overlap_count += 1
            visited[current_position + 100000] += 1

print(overlap_count)
    

