N = int(input())
a = list(map(int, input().split()))

a.sort()
a_set = set(a)  # 빠른 포함 검사

count = 0

for i in range(N):
    for j in range(i + 1, N):
        total = a[i] + a[j]
        if total % 2 == 0:
            k = total // 2
            if k not in a_set:
                count += 1

print(count)
