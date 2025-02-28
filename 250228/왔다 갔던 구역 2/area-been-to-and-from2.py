# N (명령의 수) 입력
N = int(input())

# 위치를 방문한 횟수를 기록할 딕셔너리
visited = {}

# 시작 위치
current_position = 0

# 명령에 따른 이동 처리
for _ in range(N):
    x, direction = input().split()
    x = int(x)  # 이동할 크기
    
    if direction == 'L':
        # 왼쪽으로 x만큼 이동
        for _ in range(x):
            current_position -= 1
            # 위치 방문 횟수 증가
            if current_position in visited:
                visited[current_position] += 1
            else:
                visited[current_position] = 1
    elif direction == 'R':
        # 오른쪽으로 x만큼 이동
        for _ in range(x):
            current_position += 1
            # 위치 방문 횟수 증가
            if current_position in visited:
                visited[current_position] += 1
            else:
                visited[current_position] = 1

# 2번 이상 지나간 구간의 크기 계산
overlap_count = 0
for count in visited.values():
    if count >= 2:
        overlap_count += 1

# 2번 이상 지나간 영역의 크기 출력
print(overlap_count)
