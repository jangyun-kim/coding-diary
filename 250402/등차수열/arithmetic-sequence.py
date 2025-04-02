N = int(input())
a = list(map(int, input().split()))

from collections import defaultdict

k_pair_count = defaultdict(int)

for i in range(N):
    for j in range(i + 1, N):
        total = a[i] + a[j]
        if total % 2 != 0:
            continue  # 중간값이 정수가 아니면 무시
        k = total // 2
        k_pair_count[k] += 1  # k 중심으로 등차쌍 하나 추가

# 최대 쌍 개수 출력
if k_pair_count:
    print(max(k_pair_count.values()))
else:
    print(0)
