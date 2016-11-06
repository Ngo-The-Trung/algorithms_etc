#include <iostream>
#include <vector>

using namespace std;

int main()
{
    long M, N;
    cin >> N >> M;
    vector<long> coins(M);

    for (long i = 0; i < M; ++i) {
        if (N == 0) {
            cout << 0 << endl;
            return 0;
        }

        cin >> coins[i];
    }
    vector< vector<long> > a;
    a.resize(M);
    for (long i = 0; i < M; ++i) {
        a[i].resize(N + 1);
        for (long j = 0; j <= N; ++j) {
            if (i == 0) a[i][j] = j % coins[i] == 0 ? 1 : 0;
            else {
                a[i][j] = 0;
                for (long k = 0; k < 1 + j / coins[i]; k++) {
                    a[i][j] += a[i - 1][j - coins[i] *k];
                };
            }
        }
    }
    cout << a[M - 1][N] << endl;
    return 0;
}
