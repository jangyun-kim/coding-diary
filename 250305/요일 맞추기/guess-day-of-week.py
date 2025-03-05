m1, d1, m2, d2 = map(int, input().split())

# 기준일의 요일 (2011년 m1월 d1일이 월요일)
today = 1  # 월요일 (0: 일요일, 1: 월요일, ..., 6: 토요일)
cnt_day = 0  # 날짜 차이 계산

# 월별 날짜 (2011년은 윤년이 아님)
date_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

def days_between(m1, d1, m2, d2):
    ## 두 날짜 사이의 거리(일수)를 반환
    total_days = 0
    forward = (m1, d1) < (m2, d2)  ## True이면 m1, d1 → m2, d2 (미래 이동)

    while (m1, d1) != (m2, d2):
        if forward:
            d1 += 1
            if d1 > date_of_month[m1]:  ## 월이 넘어가면
                d1 = 1
                m1 += 1
        else:
            d1 -= 1
            if d1 < 1:  ## 월이 넘어가면
                m1 -= 1
                d1 = date_of_month[m1]

        total_days += 1

    return total_days if forward else -total_days  ## 미래면 양수, 과거면 음수

# 날짜 차이 계산
cnt_day = days_between(m1, d1, m2, d2)

# 최종 요일 계산
target_day = (today + cnt_day) % 7
print(day_of_week[target_day])