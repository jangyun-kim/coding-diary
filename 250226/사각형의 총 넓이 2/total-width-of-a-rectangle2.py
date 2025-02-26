n = int(input())
arr = [[0 for i in range(210)] for i in range(210)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    
    for x in range(a, c):
        for y in range(b, d):
            arr[x][y] = 1

cnt = 0
for i in range(210):
    for j in range(210):
        if arr[i][j] == 1:
            cnt += 1

print(cnt)

