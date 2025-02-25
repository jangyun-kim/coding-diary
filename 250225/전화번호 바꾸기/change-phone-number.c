#include <stdio.h>

int main() {
    int f, m, l;
    scanf("%d-%d-%d", &f, &m, &l);
    printf("%03d-%d-%d", f, l, m);
    return 0;
}