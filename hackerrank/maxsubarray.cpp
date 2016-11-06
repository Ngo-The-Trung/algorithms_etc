#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int T, N;

    const int min = -10000 - 1;

    cin >> T;
    for (int _i = 0; _i < T; ++_i) {
        cin >> N;

        int max2 = min, max1 = min, v;
        int max_last = 0;
        for (int i = 0; i < N; ++i) {
            cin >> v;

            if (v > max1) max1 = v;

            if (max_last + v > 0) {
                max_last += v;
                if (max_last > max1) {
                    max1 = max_last;
                }
            } else {
                max_last = 0;
            }

            if (v > 0) {
                if (max2 < 0) {
                    max2 = v;
                } else {
                    max2 += v;
                }
            } else if (v > max2) max2 = v;
        }
        cout << max1 << " " << max2 << endl;

    }

    return 0;
}
