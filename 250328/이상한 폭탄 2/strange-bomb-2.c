#include <stdio.h>

#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

int boombs[100];

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    int N, K;
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; i++) {
        scanf("%d", &boombs[i]);
    }
    
    int boom = -1;

    for (int i = 0; i < N; i++) {
        for (int j = 1; j + K < N; j++) {
            if (boombs[i] == boombs[j]) {
                boom = MAX(boom, boombs[i]);
            }
        }
    }
    
    printf("%d", boom);
    return 0;
}