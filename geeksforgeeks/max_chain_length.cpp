#include <iostream>
#include <algorithm>

struct val{
	int first;
	int second;
};

int maxChainLen(struct val p[], int n)
{
    std::sort(p, p + n, [](struct val a, struct val b) {
        return (a.first < b.first || (a.first == b.first && a.second < b.second));
    });
    int best[n], max = 1;

    for (int i = 0; i < n; ++i) {
        best[i] = 1;
    }

    for (int i = 1; i < n; ++i) {
        for (int j = 0; j < i; ++j) {
            if (p[i].first > p[j].second && best[i] < best[j] + 1)
            {
                best[i] = best[j] + 1;
            }
        }
        if (best[i] > max) max = best[i];
    }
    return max;
}

int main(int argc, char *argv[])
{
    struct val p1[] = {{5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90}};
    struct val p2[] = {{5, 10} , {1, 11}};
    struct val p3[] = {{778, 887}, {794, 916}, {336, 387}, {493, 650}, {363, 422}, {28, 691}, {60, 764}, {541, 927}, {173, 427}, {212, 737}, {369, 568}, {430, 783}, {531, 863}, {68, 124}, {136, 930}, {23, 803}, {59, 70}, {168, 394}, {12, 457}, {43, 230}, {374, 422}, {785, 920}, {199, 538}, {316, 325}, {371, 414}, {92, 527}, {957, 981}, {863, 874}, {171, 997}, {282, 306}, {85, 926}, {328, 337}, {506, 847}, {314, 730}};
    std::cout << maxChainLen(p1, 5) << std::endl;
    std::cout << maxChainLen(p2, 2) << std::endl;
    std::cout << maxChainLen(p3, 34) << std::endl;
    return 0;
}
