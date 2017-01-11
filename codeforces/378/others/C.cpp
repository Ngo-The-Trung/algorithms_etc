// mjy0724's solution

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
typedef long long ll;
#define rep(i, a, b) for (int i = a; i <= b; ++ i)  // uses <= for repetition, probably uses 1-based indexing a lot
const int maxn = 510;
using namespace std;
int n,k,a[maxn],b[maxn],sa[maxn],sb[maxn];
int tot,num[maxn];
char dir[maxn];
bool solve(int l,int r,int k) {
	int maxv=0,pos=-1;
	rep(i,l,r) maxv=max(maxv,a[i]);
	rep(i,l,r) {
		if (a[i]==maxv&&((i!=l&&a[i]>a[i-1])||(i!=r&&a[i]>a[i+1]))) {
			pos=i;
			break;
		}
	}
//	printf("%d %d\n",maxv,pos);
	if (pos==-1) return 0;
	if (pos!=l&&a[pos]>a[pos-1]) {
		for (int i=pos;i>l;i--) {
			num[++tot]=i-l+k;
			dir[tot]='L';
		}
		for (int i=pos;i<r;i++) {
			num[++tot]=k;
			dir[tot]='R';
		}
	} else {
		for (int i=pos;i<r;i++) {
			num[++tot]=pos-l+k;
			dir[tot]='R';
		}
		for (int i=pos;i>l;i--) {
			num[++tot]=i-l+k;
			dir[tot]='L';
		}
	}
	return 1;
}
int main() {
	scanf("%d",&n);
	rep(i,1,n) scanf("%d",&a[i]),sa[i]=sa[i-1]+a[i];
	scanf("%d",&k);
	rep(i,1,k) scanf("%d",&b[i]),sb[i]=sb[i-1]+b[i];
	if (sa[n]!=sb[k]) {
		puts("NO");
		return 0;
	}
	int pre=0;
	rep(i,1,k) {
		bool found=0;
		rep(j,1,n) if (sa[j]==sb[i]) {  // elegant summing check
			found=1;
			if (!solve(pre+1,j,i)) {
				puts("NO");
				return 0;
			}
			pre=j;
		}
		if (!found) {
			puts("NO");
			return 0;
		}
	}
	puts("YES");
	rep(i,1,n-k) {
		printf("%d %c\n",num[i],dir[i]);
	}
	return 0;
}
