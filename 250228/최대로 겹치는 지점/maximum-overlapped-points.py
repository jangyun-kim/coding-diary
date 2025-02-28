n = int(input())
segments = []

for _ in range(n):
    start, end = map(int, input().split())
    segments.append((start, 1))
    segments.append((end + 1, -1))

segments.sort(key=lambda x: (x[0], x[1]))

max_overlap = 0
current_overlap = 0

for segment in segments:
    current_overlap += segment[1]
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)



