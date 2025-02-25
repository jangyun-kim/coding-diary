#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    double sum = a + b;
    double sub = a - b;

    printf("%.2f", sum / sub);
    return 0;
}