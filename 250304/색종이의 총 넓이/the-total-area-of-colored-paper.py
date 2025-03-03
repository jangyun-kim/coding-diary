# 색종이가 붙여진 총 넓이를 구하는 프로그램
def count_colored_area(arr, N, papers):
    for x, y in papers:
        for i in range(x, x + 8):  # 가로 8칸
            for j in range(y, y + 8):  # 세로 8칸
                arr[i][j] = 1  # 색종이가 붙은 영역 표시
    
    return sum(sum(row) for row in arr)  # 1이 표시된 영역의 총합

# 좌표 범위 조정 (-100, -100)을 (0,0)으로 변환
offset = 100
total_size = 201  # (-100, -100) ~ (100,100)을 포함하는 크기
arr = [[0 for _ in range(total_size)] for _ in range(total_size)]

# 입력 받기
N = int(input())
papers = [tuple(map(lambda x: int(x) + offset, input().split())) for _ in range(N)]

# 색종이가 덮은 총 넓이 계산
colored_area = count_colored_area(arr, N, papers)

# 결과 출력
print(colored_area)