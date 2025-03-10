n = int(input())
people = [tuple(input().split()) for _ in range(n)]
pos = [int(p[0]) for p in people]
alpha = [p[1] for p in people]

max_length = 0
prefix_sum = 0
index_map = {0: -1}  # First occurrence of each prefix sum

for i in range(n):
    prefix_sum += 1 if alpha[i] == 'G' else -1

    if prefix_sum in index_map:
        max_length = max(max_length, pos[i] - pos[index_map[prefix_sum]])
    else:
        index_map[prefix_sum] = i

print(max_length)