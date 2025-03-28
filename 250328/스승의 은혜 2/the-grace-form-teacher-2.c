#include <stdio.h>
#include <stdlib.h>

#define MAX_N 1000
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

int N, B;
int p[MAX_N];

int compare(const void* a, const void* b) {
    return (*(int*)a - *(int*)b);
}

int main() {
    scanf("%d %d", &N, &B);
    for (int i = 0; i < N; i++) {
        scanf("%d", &p[i]);
    }
    
    int max_gift = 0;

    for (int k = 0; k < N; k++) {
        int temp[MAX_N];
        for (int i = 0; i < N; i++) temp[i] = p[i];
        
        temp[k] /= 2;
        qsort(temp, N, sizeof(int), compare);

        int total = 0;
        int count = 0;

        for (int i = 0; i < N; i++) {
            total += temp[i];

            if (total > B) break;
            count++;

        }
        
        max_gift = MAX(max_gift, count);
    }

    printf("%d", max_gift);
    
    return 0;
}