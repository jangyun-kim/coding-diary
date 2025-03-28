#include <iostream>
#include <algorithm>

using namespace std;

int N, B;
int P[1000];

int main() {
    cin >> N >> B;

    for (int i = 0; i < N; i++) {
        cin >> P[i];
    }

    
    int max_gifted = 0;

    for (int k = 0; k < N; k++) {
        int temp[1000];
        for (int i = 0; i < N; i++) temp[i] = P[i];

        temp[k] /= 2;
        std::sort(temp, temp + N);

        int total = 0;
        int count = 0;

        for (int i = 0; i < N; i++) {
            total += temp[i];

            if (total > B) break;
            count++;
        }

        max_gifted = max(max_gifted, count);
    }

    cout << max_gifted;

    return 0;
}