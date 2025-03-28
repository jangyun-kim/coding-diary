#include <iostream>

using namespace std;

int N, K;
int boombs[100];

int main() {
    cin >> N >> K;

    for (int i = 0; i < N; i++) {
        cin >> boombs[i];
    }

    int boom = -1;
    for (int i = 0; i < N; i++) {
        for (int j = 1; j <= K; j++) {
            if (boombs[i] == boombs[i + j]) {
                boom = max(boom, boombs[i]);
            }
        }
    }

    cout << boom;
    return 0;
}