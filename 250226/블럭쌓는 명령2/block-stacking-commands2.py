N, K = map(int, input().split())
h = [0 for i in range(N + 1)]

for i in range(K):
    a, b = map(int, input().split())

    for j in range(a, b + 1):
        h[j] += 1

answer = 0
for i in range(1, N + 1):
    if answer < h[i]:
        answer = h[i]

print(answer)