import sys

INT_MIN = -sys.maxsize

n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

def initialize():
    for i in range(1, n + 1):
        dp[i] = INT_MIN
    dp[1] = arr[1]

initialize()

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])

ans = max(dp[1:n + 1])


print(ans)