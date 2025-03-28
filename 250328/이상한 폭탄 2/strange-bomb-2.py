N, K = map(int, input().split())
boombs = [int(input()) for _ in range(N)]

boom = 0
for i in range(N):
    for j in range(i + 1, min(i + K + 1, N)):
        if boombs[i] == boombs[j]:
            boom = max(boom, boombs[i])

print(boom)

            

