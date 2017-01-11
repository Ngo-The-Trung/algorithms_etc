#include <assert.h>
#include <stdint.h>
#include <stdio.h>

int32_t JumpConsistentHash(uint64_t key, int32_t num_buckets)
{
    int64_t b = -1, j = 0;
    while (j < num_buckets) {
        b = j;
        key = key * 2862933555777941757ULL + 1;
        j = (b + 1) * (double(1LL << 31) / double((key >> 33) + 1));
    }
    return b;
}

void TestJumpConsistentHash()
{
    const int32_t MAX = 1000, buckets = 100;
    int32_t keys100[MAX], tmp;
    for (int i = 1; i <= MAX; ++i) {
        keys100[i] = JumpConsistentHash((uint64_t)i, buckets);
    }
    for (int i = 1; i <= MAX; ++i) {
        tmp = JumpConsistentHash((uint64_t)i, buckets + 1);
        if (keys100[i] != tmp) {
            printf("%d moved from %d to %d\n", i, keys100[i], tmp);
        }
    }
}

int main(int argc, char *argv[])
{
    TestJumpConsistentHash();
    return 0;
}
