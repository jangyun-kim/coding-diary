#include <stdio.h>

int main() {
    int A, B;
    scanf("%d %d", &A, &B);
    printf("%d %.1f", A+B, (double)(A+B)/2);
    return 0;
}