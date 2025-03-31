#include <stdio.h>
#include <string.h>

int is_interesting(int num) {
    int freq[10] = {0};
    char str[12];  // int 범위 내 숫자를 문자열로 바꿔 저장
    sprintf(str, "%d", num);

    int len = strlen(str);

    // 각 숫자 빈도수 계산
    for (int i = 0; i < len; i++) {
        int digit = str[i] - '0';
        freq[digit]++;
    }

    int unique_digits = 0;
    int counts[2]; // 등장하는 두 숫자의 빈도 저장
    int idx = 0;

    for (int i = 0; i < 10; i++) {
        if (freq[i] > 0) {
            unique_digits++;
            if (idx < 2) {
                counts[idx++] = freq[i];
            }
        }
    }

    if (unique_digits != 2) {
        return 0;
    }

    // 정렬 없이 조건 확인
    int a = counts[0], b = counts[1];
    if ((a == 1 && b == len - 1) || (b == 1 && a == len - 1)) {
        return 1;
    }

    return 0;
}

int count_interesting_numbers(int X, int Y) {
    int count = 0;
    for (int num = X; num <= Y; num++) {
        if (is_interesting(num)) {
            count++;
        }
    }
    return count;
}

int main() {
    int X, Y;
    scanf("%d %d", &X, &Y);

    int result = count_interesting_numbers(X, Y);
    printf("%d\n", result);

    return 0;
}