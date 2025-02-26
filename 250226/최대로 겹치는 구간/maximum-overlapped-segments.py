OFFSET = 100
MAX_R = 200

n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
checked = [0] * (MAX_R + 1)

for x1, x2 in segments:
    x1, x2 = x1 + OFFSET, x2 + OFFSET
    
    for i in range(x1, x2):
        checked[i] += 1

# 최댓값을 구합니다.
max_num = max(checked)
print(max_num)
