#include <stdio.h>

int main() {
    int N = 0;
    scanf("%d", &N);

    if (N < 0) {
        printf("%d\n", N);
        printf("minus");
    }
    else {
        printf("%d", N);
    }

    return 0;
}