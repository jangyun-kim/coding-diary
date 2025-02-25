#include <stdio.h>

int main() {
    int a = 5, b = 6, c = 7;
    int temp;

    temp = a;
    a = c;
    c = b;
    b = temp;

    printf("%d\n", a);
    printf("%d\n", b);
    printf("%d", c);
    return 0;
}