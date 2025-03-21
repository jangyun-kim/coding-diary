MAX_NUM = 1000

N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    count = [0] * MAX_NUM
    for j, (l, r) in enumerate(times):
        if j == i:
            continue
        
        for k in range(l, r):
            count[k] += 1

    time = 0

    for j in range(1, MAX_NUM):
        if count[j] > 0:
            time += 1

    ans = max(ans, time)

print(ans)