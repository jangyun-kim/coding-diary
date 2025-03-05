X, Y = map(int, input().split())

ans = 0
# 탐색해야 하는 범위
# X ~ Y까지의 수
for num in range(X, Y+1):
    # 할거하자
    # 각 자리수의 합을 구하자
    # 232
    num = str(num)
    # '232'
    num = list(num)
    # ['2', '3', '2']
    num = list(map(int, num))
    #[2, 3, 2]
    num = sum(num)
    # 7
    ans = max(ans, num)

print(ans)