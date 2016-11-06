#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int main(void)
{
    int N;
    cin >> N;
    vector<int> A, M;
    A.reserve(N);
    M.reserve(N);
    fill(M.begin(), M.begin() + N, 0);

    int L = 0;
    for (int i = 0; i < N; ++i) {
        cin >> A[i];

        int left = 1, right = L, mid;
        while (left <= right) {
            mid = (left + right) / 2;
            if (A[M[mid]] < A[i]) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        M[left] = i;
        if (left > L) L = left;
    }
    cout << L << endl;
    return 0;
}
