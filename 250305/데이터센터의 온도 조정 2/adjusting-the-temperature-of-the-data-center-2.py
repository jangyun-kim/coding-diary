N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

def work(tmp, T_a, T_b):
    # 선호 온도가 T_a ~ T_b일 때
    # 현재 온도가 t라면
    # 얼마만큼의 작업량을 얻을 수 있는지 반환하는 함수
    if tmp < T_a:
        return C
    elif T_a <= tmp <= T_b:
        return G
    else:
        return H

# ans = 0
# # 0에서 1000까지 모든 범위에 대해 탐색
# for tmp in range(0, 1001):
#     # N개의 장비에 대해 각각 작업량을 계산하여 누적\
#     total_work = 0
#     for i in range(N):
#         total_work += work(tmp, ranges[i][0], ranges[i][1])

#     ans = max(ans, total_work)

# print(ans)

# Python에서 조금 더 좋은 방식
ans = 0
# 0에서 1000까지 모든 범위에 대해 탐색
for tmp in range(0, 1001):
    # N개의 장비에 대해 각각 작업량을 계산하여 누적\
    total_work = sum([
        work(tmp, T_a, T_b)
        for T_a, T_b in ranges
    ])

    ans = max(ans, total_work)

print(ans)