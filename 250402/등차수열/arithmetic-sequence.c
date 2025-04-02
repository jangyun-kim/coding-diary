#include <stdio.h>

#define MAX_N 100
#define MAX_K 100

int N;
int arr[MAX_N];
int k_count[MAX_K + 1] = {0};

int main() {
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &arr[i]);
    }
    

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            int total = arr[i] + arr[j];
            if (total % 2 != 0) {
                continue;
            }
            int k = total / 2;

            if (k <= MAX_K) {
                k_count[k]++;
            }
        }
    }

    int max_count = 0;
    for (int i = 0; i <= MAX_K; i++) {
        if (k_count[i] > max_count) {
            max_count = k_count[i];
        }
    }

    printf("%d", max_count);
    
    return 0;
}