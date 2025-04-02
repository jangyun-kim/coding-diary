N = int(input())
a = list(map(int, input().split()))

a_set = set(a)
k_count = {}

for i in range(N):
    for j in range(i + 1, N):
        total = a[i] + a[j]
        if total % 2 != 0:
            continue  # 중간값 k가 정수가 아님
        k = total // 2
        if k in a_set:
            continue  # 리스트에 이미 있는 값은 제외

        if k not in k_count:
            k_count[k] = 1
        else:
            k_count[k] += 1

# 최대 등장 개수 출력
if k_count:
    print(max(k_count.values()))
else:
    print(0)
