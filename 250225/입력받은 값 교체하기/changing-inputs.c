#include <stdio.h>

int main() {
    int a, b;
    int temp;
    scanf("%d %d", &a, &b);

    temp = a;
    a = b;
    b = temp;

    printf("%d %d", a, b);
    return 0;
}