#include <stdio.h>
#include <string.h>

#define MAX_N 100

int N;
char A[MAX_N][4];
int B[MAX_N], C[MAX_N];

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        int num;
        scanf("%d %d %d", &num, &B[i], &C[i]);
        snprintf(A[i], 4, "%03d", num);
    }

    int valid_count = 0;
    
    for (int a = 1; a < 10; a++) {
        for (int b = 1; b < 10; b++) {
            if (b == a) {
                continue;
            }

            for (int c = 1; c < 10; c++) {
                if ((c == a) || (c == b)) {
                    continue;
                }

                char candidate[4];
                snprintf(candidate, 4, "%d%d%d", a, b, c);
                int is_valid = 1;

                for (int i = 0; i < N; i++) {
                    char *B_guess = A[i];
                    int expected_cnt1 = B[i];
                    int expected_cnt2 = C[i];
                    
                    // calculate cnt1: both position and number are correct
                    int cnt1 = 0;
                    for (int j = 0; j < 3; j++) {
                        if (candidate[j] == B_guess[j]) {
                            cnt1++;
                        }
                    }

                    // calculate cnt2: the position is different, but the number is the same.
                    int candidate_digits[10] = {0};
                    int B_guess_digits[10] = {0};

                    for (int j = 0; j < 3; j++) {
                        candidate_digits[candidate[j] - '0'] = 1;
                        B_guess_digits[B_guess[j] - '0'] = 1;
                    }

                    int common = 0;
                    for (int d = 0; d < 10; d++) {
                        if (candidate_digits[d] && B_guess_digits[d]) {
                            common++;
                        }
                    }

                    int cnt2 = common - cnt1;

                    if (expected_cnt1 == 0 && expected_cnt2 == 0) {
                        int found = 0;
                        for (int j = 0; j < 3; j++) {
                            for (int k = 0; k < 3; j++) {
                                if (candidate[j] == B_guess[k]) {
                                    found = 1;
                                    break;
                                }
                            }

                            if (found) {
                                break;
                            }
                        }
                        
                        if (found) {
                            is_valid = 0;
                            break;
                        }
                    } else if (cnt1 != expected_cnt1 || cnt2 != expected_cnt2) {
                        is_valid = 0;
                        break;
                    }
                }
                
                if (is_valid) {
                    valid_count++;
                }
            } 
        }
    }

    printf("%d", valid_count);
    return 0;
}