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
#define msi map<string, int>
#define mss map<string, string>
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
    char i, j, k, l, m;
    auto container = msi();
    int count = 0;
    for(i = 'a'; i <= 'z'; i++) {
        string x = "";
        x += i;
        count += 1;
        container[x] = count;
    }
    for(i = 'a'; i <= 'y'; i++) {
        for (j = i + 1; j <= 'z'; j++) {
            string x = "";
            count += 1;
            x += i; x += j;
            container[x] = count;
        }
    }
    for(i = 'a'; i <= 'x'; i++) {
        for (j = i + 1; j <= 'y'; j++) {
            for (k = j + 1; k <= 'z'; k++) {
                string x = "";
                count += 1;
                x += i; x += j; x += k;
                container[x] = count;
            }
        }
    }
    for(i = 'a'; i <= 'w'; i++) {
        for (j = i + 1; j <= 'x'; j++) {
            for (k = j + 1; k <= 'y'; k++) {
                for (l = k + 1; l <= 'z'; l++) {
                    string x = "";
                    count += 1;
                    x += i; x += j; x += k; x += l;
                    container[x] = count;
                }
            }
        }
    }
    for(i = 'a'; i <= 'v'; i++) {
        for (j = i + 1; j <= 'w'; j++) {
            for (k = j + 1; k <= 'x'; k++) {
                for (l = k + 1; l <= 'y'; l++) {
                    for (m = l + 1; m <= 'z'; m++) {
                        string x = "";
                        count += 1;
                        x += i; x += j; x += k; x += l; x += m;
                        container[x] = count;
                    }
                }
            }
        }
    }
    string input;
    while (std::getline(std::cin, input)) {
        cout << container[input] << endl;
    }
    return 0;
}
