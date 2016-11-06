#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

// left scan: start with 1 candy, if the next student has higher score, +1, else -1
// then scan right (start with 1 again). Result = max of the 2 score
int main() {
    long N;
    cin >> N;

    vector<long> v(N), result(N);
    long i_min, min = 10000 + 1;

    result[0] = 1;
    long acc = 1;
    for (long i = 0; i < N; ++i) {
        cin >> v[i];
        if (v[i] < min) {
            min = v[i];
            i_min = i;
        }
        if (i > 0) {
            if (v[i] > v[i - 1]) {
                acc += 1;
            } else {
                acc = 1;
            }
            result[i] = acc;
        }
    }
    acc = 1;
    if (result[N-1] < 1) result[N-1] = 1;
    for (long i = N - 2; i >=0; --i) {
        if (v[i] > v[i + 1]) {
            acc += 1;
        } else {
            acc = 1;
        }
        if (acc > result[i]) result[i] = acc;
    }
    long sum = 0;
    for (long i = 0; i < N; ++i) {
        sum += result[i];
    }
    cout << sum << endl;
    return 0;
}
