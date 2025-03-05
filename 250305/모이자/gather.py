import sys

N = int(input())
A = list(map(int, input().split()))

ans = sys.maxsize

# Locate each conference room at number 1 ~ N-1
# located place i
for i in range(N):
    # do: sum the distance of all people 
    dist = 0
    for j in range(N):
        dist += abs(i - j) * A[j]

    ans = min(ans, dist)
    
print(ans)