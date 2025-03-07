N, r, c = map(int, input().split())
a = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    row = list(map(int, input().split()))
    for j in range(1, N + 1):
        a[i][j] = row[j - 1]

def in_range(r, c):
    return 1 <= r <= N and 1 <= c <= N

def simulate(r, c):
    # set dr, dc in order from UDLR 
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for k in range(4):
        nr, nc = r + dr[k], c + dc[k]
    
        # nr, nc for searching in the range
        # if some values are larger than itself, then move and break
        # (move means the end of the function and recall)
        if in_range(nr, nc) and a[nr][nc] > a[r][c]:
            return (nr, nc)
        
    # cannot move anymore
    return (-1, -1)

while True:
    print(a[r][c], end=" ")
    r, c = simulate(r, c)

    if r == -1 and c == -1:
        break