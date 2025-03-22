#include <stdio.h>
#include <string.h>

#define MAX_N 1000
#define MAX_TIME 1000


int N;
int A[MAX_N], B[MAX_N];

int main() {
    scanf("%d", &N);

    for (int i = 0; i < N; i++) {
        scanf("%d %d", &A[i], &B[i]);
    }
    
    int ans = 0;

    for (int i = 0; i < N; i++) {
        int count[MAX_TIME] = {0}; // count of spending time

        for (int j = 0; j < N; j++) {
            if (j == i) {
                continue;
            }

            for (int k = A[j]; k < B[j]; k++) {
                count[k]++;
            }
        }

        int time = 0;

        for (int t = 0; t < MAX_TIME; t++) {
            if (count[t] > 0) {
                time++;
            }
        }

        if (time > ans) {
            ans = time;
        }
    }

    printf("%d", ans);
    return 0;
}