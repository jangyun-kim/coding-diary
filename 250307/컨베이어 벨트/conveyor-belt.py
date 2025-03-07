N, T = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

temp = u[N - 1]

for _ in range(T):
    temp = d[N - 1]

   
    prev = u[N - 1]
    for i in range(N - 1, 0, -1):
        u[i] = u[i - 1]
    u[0] = temp

 
    for i in range(N - 1, 0, -1):
        d[i] = d[i - 1]
    d[0] = prev

# 결과 출력
print(*u)
print(*d)