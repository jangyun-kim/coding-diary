N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

max_coins = 0 # the amount of max coin

# check the point that it is possible 3x3 grid (in the range)
for i in range(N - 2):
    for j in range(N - 2):
        coin_count = 0
        for x in range(3):
            for y in range(3):
                coin_count += grid[i + x][j + y]

        # update max coin
        max_coins = max(max_coins, coin_count)

# print result
print(max_coins)
            