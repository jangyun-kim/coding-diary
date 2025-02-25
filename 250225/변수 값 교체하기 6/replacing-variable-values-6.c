#include <stdio.h>

int main() {
    int a = 2, b= 5;
    int temp;

    temp = a;
    a = b;
    b = temp;

    printf("%d\n", a);
    printf("%d", b);
    return 0;
}