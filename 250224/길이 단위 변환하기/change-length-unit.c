#include <stdio.h>

int main() {
    double fttocm = 30.48, mitocm = 160934;
    double ft = 9.2, mi = 1.3;
    double ft_cal = ft * fttocm, mi_cal = mi * mitocm;

    printf("%.1fft = %.1fcm\n", ft, ft_cal);
    printf("%.1fmi = %.1fcm", mi, mi_cal);
    return 0;
}