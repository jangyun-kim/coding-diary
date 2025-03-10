n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

max_length = 0
prefix_sum = 0
index_map = {0: -1}  # First occurrence of each prefix sum

start = 0
for i in range(1, n):
    if alpha[i] != alpha[start]:  
        max_length = max(max_length, pos[i - 1] - pos[start])  # Compute segment length
        start = i  # Start a new segment

# Check last contiguous segment
max_length = max(max_length, pos[n - 1] - pos[start])

# Step 4: Find longest segment where `G` and `H` are balanced using prefix sum
for i in range(n):
    prefix_sum += 1 if alpha[i] == 'G' else -1

    if prefix_sum in index_map:
        max_length = max(max_length, pos[i] - pos[index_map[prefix_sum]])  # Corrected calculation
    else:
        index_map[prefix_sum] = i  # Store index instead of position

# Step 5: Print the correct result
print(max_length)