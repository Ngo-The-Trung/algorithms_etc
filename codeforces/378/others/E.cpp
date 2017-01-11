
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll;
#define rep(i, a, b) for (int i = a; i <= b; ++ i)
const int maxn = 1000010;
using namespace std;

char s[maxn];
int n, cu[maxn], cd[maxn];
ll su[maxn], sd[maxn], pu[maxn], pd[maxn];
int main() {
	scanf("%d", &n);
	scanf("%s", s + 1);
	rep(i, 1, n) {
		cu[i] = cu[i - 1] + (s[i] == 'U');
		cd[i] = cd[i - 1] + (s[i] == 'D');
		su[i] = su[i - 1] + (s[i] == 'U') * i;
		sd[i] = sd[i - 1] + (s[i] == 'D') * i;
		pu[cu[i]] = su[i];
		pd[cd[i]] = sd[i];
	}
	rep(i, 1, n) {
		if (s[i] == 'U') {
			int dr = cd[n] - cd[i - 1], ul = cu[i - 1];
			if (ul < dr) {
				printf("%lld ", 2 * (pd[cd[i] + ul + 1] - sd[i]) - i - 2 * su[i - 1]);
			} else {
				printf("%lld ", n + 1 + 2 * (sd[n] - sd[i]) - i - 2 * (su[i - 1] - pu[cu[i - 1] - dr]));
			}
		} else {
			int dr = cd[n] - cd[i], ul = cu[i - 1];
			if (ul <= dr) {
				printf("%lld ", 2 * (pd[cd[i] + ul] - sd[i]) + i - 2 * su[i - 1]);
			} else {
				printf("%lld ", n + 1 + 2 * (sd[n] - sd[i]) + i - 2 * (su[i - 1] - pu[cu[i - 1] - dr - 1]));
			}
		}
	}
	puts("");
	return 0;
}
