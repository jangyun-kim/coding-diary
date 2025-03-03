A, B, C = map(int, input().split())

total_time_flow = (A * 24 * 60 + B * 60 + C) - (11 * 24 * 60 + 11 * 60 + 11)

if total_time_flow < 0:
    print(-1)
else:
    print(total_time_flow)