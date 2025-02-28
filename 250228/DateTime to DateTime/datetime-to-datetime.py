A, B, C = map(int, input().split())

initial_day = 11
initial_hour = 11
initial_minute = 11
cnt_time = 0
cnt_date = 0

# 초기 시각의 총 분
initial_total_minutes = (initial_day - 1) * 1440 + initial_hour * 60 + initial_minute

# 목표 시각의 총 분
target_total_minutes = (A - 1) * 1440 + B * 60 + C

# 흐른 시간
total_time_flow = target_total_minutes - initial_total_minutes

print(total_time_flow)
