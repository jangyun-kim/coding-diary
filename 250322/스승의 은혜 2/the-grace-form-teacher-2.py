N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()
max_gifted = 0

for i in range(N):
    total = 0
    count = 0

    for j in range(N):
        if j == i:
            total += P[j] // 2 # using coupon
        else:
            total += P[j]

        if total > B:
            break
        count += 1

        max_gifted = max(max_gifted, count)

print(max_gifted)