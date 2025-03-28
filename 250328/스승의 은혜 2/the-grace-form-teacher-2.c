#include <stdio.h>

#define MAX_N 1000
#define MAX(X,Y) ((X) > (Y) ? (X) : (Y))

int N, B;
int p[MAX_N];

int main() {
    scanf("%d %d", &N, &B);
    for (int i = 0; i < N; i++) {
        scanf("%d", &p[i]);
    }
    
    int max_gift = 0;

    for (int i = 0; i < N; i++) {
        int total = 0;
        int count = 0;

        for (int j = 0; j < N; j++) {
            if (j == i) {
                total += p[j] / 2;
            }
            else {
                total += p[j];
            }

            if (total > B) {
                break;
            }

            count += 1;

            max_gift = MAX(max_gift, count);
        }
    }

    printf("%d", max_gift);
    
    return 0;
}