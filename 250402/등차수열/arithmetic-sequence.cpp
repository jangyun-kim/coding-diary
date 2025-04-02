#include <iostream>

#define MAX_N 100
#define MAX_K 100

using namespace std;

int N;
int arr[MAX_N];
int k_count[MAX_K + 1] = {0};
int k;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            int total = arr[i] + arr[j];
            if (total % 2 != 0) {
                continue;
            }

            k = total / 2;
            if (k <= MAX_K) {
                k_count[k]++;
            }
        }
    }

    int max_count = 0;
    for (int i = 0; i <= MAX_K; i++) {
        if (k_count[i] > max_count) {
            max_count = k_count[i];
        }
    }

    cout << max_count;

    return 0;
}