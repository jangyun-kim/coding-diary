N = int(input())
h = [0 for i in range(110)]

for i in range(N):
    x1, x2 = map(int, input().split())

    for j in range(x1, x2):
        h[j] += 1

answer = 0
for i in range(110):
    if answer < h[i]:
        answer = h[i]

print(answer)