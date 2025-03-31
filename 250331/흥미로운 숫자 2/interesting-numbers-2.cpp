#include <iostream>

using namespace std;

int X, Y;

int is_interesting(int num) {
    int freq[10] = {0};
    char str[12];
    int digits[10];
    int len = 0;

    int temp = num;
    while (temp > 0) {
        int digit = temp % 10;
        freq[digit]++;
        digits[len++] = digit;
        temp /= 10;
    }

    if (len < 2) return 0;

    int unique_digits = 0;
    int counts[2];
    int idx = 0;

    for (int i = 0; i < 10; i++) {
        if(freq[i] > 0) {
            unique_digits++;
            if (idx < 2) {
                counts[idx++] = freq[i];
            }
        }
    }

    if (unique_digits != 2) return 0;

    int a = counts[0], b = counts[1];
    if ((a == 1 && b == len - 1) || (b == 1 && a == len - 1)) {
        return 1;
    }

    return 0;
}

int count_interesting_numbers(int X, int Y) {
    int count = 0;
    for (int num = X; num <= Y; num++) {
        if (is_interesting(num)) {
            count++;
        }
    }

    return count;
}

int main() {
    cin >> X >> Y;

    int result = count_interesting_numbers(X, Y);
    cout << result;
    

    return 0;
}