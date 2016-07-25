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
    auto container = hii();
    auto keys = vi();
    int i;
    while (cin >> i) {
        if (!_Mhas(container, i)) {
            container[i] = 1;
            keys.push_back(i);
        } else {
            container[i] += 1;
        }
    }
    for (size_t i = 0; i < keys.size(); ++i) {
        cout << keys[i] << " " << container[keys[i]] << endl;
    }
    return 0;
}

