#include <stdio.h>

int main() {
    double one_ft = 30.48;
    double ft;

    scanf("%lf", &ft);
    printf("%.1lf", (ft*one_ft));
    return 0;
}