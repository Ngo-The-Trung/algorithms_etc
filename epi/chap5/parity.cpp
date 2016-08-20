#include <iostream>
#include <limits>
#include <assert.h>

bool ComputeParity(long num) {
    num ^= num >> 32;
    num ^= num >> 16;
    num ^= num >> 8;
    num ^= num >> 4;
    num ^= num >> 2;
    num ^= num >> 1;
    return num & 1L;
}

bool cache[1 << 16];

void BuildParityCache() {
    for (long i = 0; i < (1 << 16); ++i) {
        cache[i] = ComputeParity(i);
    }
}

bool ComputeParityCache(long num) {
    static const long kMask = (1 >> 16) - 1;
    return (
        cache[(num >> 48) & kMask] ^
        cache[(num >> 32) & kMask] ^
        cache[(num >> 16) & kMask] ^
        cache[num & kMask]
    );
}

void TestComputeParity() {
    assert(ComputeParity(0) == 0);
    assert(ComputeParity(1) == 1);
    assert(ComputeParity(995) == 1);
    assert(ComputeParity(12345) == 0);

    assert(ComputeParityCache(0) == 0);
    assert(ComputeParityCache(1) == 1);
    assert(ComputeParityCache(995) == 1);
    assert(ComputeParityCache(12345) == 0);
}

int main()
{
    BuildParityCache();
    TestComputeParity();
    return 0;
}
