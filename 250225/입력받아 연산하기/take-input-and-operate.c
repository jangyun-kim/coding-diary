#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);
    a += 87;
    b %= 10;

    printf("%d\n", a);
    printf("%d", b);

    return 0;
}