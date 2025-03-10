MAX_NUM = 100

# set input
N = int(input())
arr = [0] * (MAX_NUM + 1)

# set position and alphabet
for _ in range(N):
    position, alph = tuple(input().split())
    position = int(position)

    arr[position] = 1 if alph == 'G' else 2

# set start point
max_len = 0
for i in range(MAX_NUM + 1):
    for j in range(i + 1, MAX_NUM + 1):
        # check person at i or j
        if arr[i] == 0 or arr[j] == 0:
            continue

        # count the number of g and h in the range
        cnt_G = 0
        cnt_H = 0

        for k in range(i, j + 1):
            if arr[k] == 1:
                cnt_G += 1
            elif arr[k] == 2:
                cnt_H += 1

        # when satisfied condition, calculate the length of the range and compare with max_val
        if cnt_G == 0 or cnt_H == 0 or cnt_G == cnt_H:
            range_len = j - i
            max_len = max(max_len, range_len)

print(max_len)