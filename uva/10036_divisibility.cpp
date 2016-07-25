#include <algorithm>
#include <bitset>
#include <climits>
#include <iostream>
#include <set>
#include <map>
#include <unordered_map>
#include <vector>

using namespace std;

#define vi vector<int>
#define vs vector<string>
#define mii map<int, int>
#define msi map<string, int>
#define mss map<string, string>
#define hii unordered_map<int, int>
#define hsi unordered_map<string, int>
#define hss unordered_map<string, string>

#define _Del(X, Y)      (X).erase((X).begin() + (Y))
#define _Ins(X, A, P)   (X).insert((X).begin() + (P), (A))
#define _Find(X, Y)     (find((X).begin(), (X).end(), (Y)))
#define _FindS(X, Y, Z) (find((Z), (X).end(), (Y)))
#define _Has(X, Y)      (find((X).begin(), (X).end(), (Y)) != (X).end())

#define _Mfind(X, Y)    ((X).find((Y)))
#define _Mhas(X, Y)     ((X).find((Y)) != (X).end())

#define _S(fun, X, Y)   (fun((X).begin(), (X).end(), (Y)))
#define _Sort(X)        std::sort((X).begin(), (X).end())

int main()
{
    int ntests, N, K;
    vi list;
    cin >> ntests;
    while (ntests --) {
        cin >> N >> K;
        int M = N;

        list.clear();
        int tmp;
        while (M--) {
            cin >> tmp;
            list.push_back(tmp);
        }

        int a[2][2 * 100 + 1];
        int cur = 0;
#define off(b) a[cur][b + 100]
#define off_next(b) a[next][b + 100]

        for (int j = -100; j < 100; j++) {
            off(j) = 0;
        }
        off(0) = 1;
        for (int i = 0; i < N; ++i) {
            int next = 1 - cur;

            for (int j = -100; j <= 100; j++) {
                off_next(j) = 0;
            }

            for (int j = -100; j <= 100; j++) {
                if (off(j) == 1) {
                    off_next( (j + list[i]) % K ) = 1;
                    off_next( (j - list[i]) % K ) = 1;
                }
            }

            cur = 1 - cur;
        }
        bool found = false;
        for (int j = -100; j <= 100; j++) {
            if (off(j) == 1 && j % K == 0) {
                cout << "Divisible\n";
                found = true;
                break;
            }
        }
        if (!found) cout << "Not divisible\n";
    }
    return 0;
}
