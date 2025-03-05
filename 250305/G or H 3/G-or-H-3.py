n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

ans = 0
for start in range(1, 10000-k+1):
    end = start + k
    #  구간 [start, end] 내의 G, H의 개수를 세서 점수를 구한다.
    score = 0
    # 모든 G, H에 대해 구간 내에 있는지 확인
    for i in range(n):
        if start <= x[i] <= end:
            if c[i] == 'G':
                score += 1
            else:
                score += 2

    ans = max(ans, score)

print(ans)
