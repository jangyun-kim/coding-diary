N = int(input())
a, b, c = map(int, input().split())

cnt = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, N+1):
            # 할거하자
            # 입력으로 주어진 자물쇠가 열리는지 확인
            # i-a, j-b, k-c 중 하나라도 2 이내면 열림
            if abs(i-a) <= 2 or abs(j-b) <= 2 or abs(k-c) <= 2:
                cnt += 1
print(cnt)                