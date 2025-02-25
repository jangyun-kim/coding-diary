#include <stdio.h>

int main() {
    int width, height;
    scanf("%d %d", &width, &height);

    width += 8;
    height *= 3;

    printf("%d\n", width);
    printf("%d\n", height);
    printf("%d", width * height);
    return 0;
}