A, B, C = map(int, input().split())

day = 11
hour = 11
minite = 11
cnt_time = 0
cnt_date = 0

# 흐르는 시간 게산
while True:
    if day == A and hour == B and minite == C:
        break

    cnt_time += 1
    minite += 1

    if minite == 60:
        hour += 1
        minite = 0

    if hour == 24:
        day += 1
        hour = 0
    
total_time_flow = cnt_time + cnt_date

print(total_time_flow)